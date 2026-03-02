import random

# Classe responsável por controlar os produtos adicionados pelo cliente
class Carrinho:
    def __init__(self):
        self.produtos = []      # Lista que armazena os produtos no carrinho
        self.desconto = 0       # Percentual de desconto aplicado
        self.cupons = random.randint(0, 3)  # Quantidade aleatória de cupons

    # Adiciona um produto ao carrinho
    def adicionar_produto(self, produto):
        # Verifica se o produto já existe no carrinho
        for p in self.produtos:
            if p.nome.lower() == produto.nome.lower():
                # Se existir, apenas soma a quantidade
                p.quantidade += produto.quantidade
                print("Quantidade atualizada.")
                return

        # Caso não exista, adiciona como novo item
        self.produtos.append(produto)
        print("Produto adicionado.")

    # Remove produto do carrinho
    def remover_produto(self, produtos):
        if not self.produtos:
            print("Carrinho vazio.")
            return

        print("\nProdutos no carrinho:")
        for i, produto in enumerate(self.produtos):
            print(f"{i+1} - {produto.nome} | Quantidade: {produto.quantidade}")

        try:
            escolha = int(input("Escolha o número do produto: ")) - 1

            # Validação da escolha
            if escolha < 0 or escolha >= len(self.produtos):
                print("Ação inválida.")
                return

            produto = self.produtos[escolha]
            qtd = int(input("Quantidade que deseja retirar: "))

            if qtd <= 0:
                print("Quantidade inválida.")
                return

            # Devolve a quantidade removida para o estoque principal
            for p in produtos:
                if p["nome"].lower() == produto.nome.lower():
                    p["estoque"] += qtd
                    break

            # Remove totalmente ou apenas reduz a quantidade
            if qtd >= produto.quantidade:
                self.produtos.remove(produto)
                print("Produto removido do carrinho.")
            else:
                produto.quantidade -= qtd
                print("Quantidade atualizada.")

        except ValueError:
            print("Entrada inválida.")

    # Lista todos os produtos do carrinho
    def listar_produtos(self):
        if not self.produtos:
            print("Carrinho vazio.")
            return

        print("\n Carrinho de Compras")
        for produto in self.produtos:
            print(f"{produto.nome} | R$ {produto.preco:.2f} | Qtd: {produto.quantidade}")
            print(f"Subtotal: R$ {produto.subtotal():.2f}")
            print("-" * 25)

        print(f"Total: R$ {self.calcular_total():.2f}")

    # Soma todos os subtotais dos produtos
    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.subtotal()
        return total

    # Aplica desconto caso o usuário tenha cupom
    def aplicar_desconto(self):
        if self.cupons <= 0:
            print("infelizmente cliente, senhor não possui cupons disponíveis.")
            return

        usar = input("Deseja usar um cupom? (s/n): ").lower()

        if usar == "s":
            percentual = random.randint(5, 30)
            self.desconto = percentual
            self.cupons -= 1
            print(f"Cupom de {percentual}% aplicado.")
        else:
            print("Cupom não utilizado.")

    # Calcula total já com desconto aplicado
    def calcular_total_com_desconto(self):
        total = self.calcular_total()
        desconto_valor = total * self.desconto / 100
        return total - desconto_valor

    # Gera a nota fiscal final da compra
    def gerar_nota_fiscal(self):
        if not self.produtos:
            print("Carrinho vazio.")
            return

        print("\nNota Fiscal")

        for produto in self.produtos:
            print(
                f"{produto.nome} - R$ {produto.preco:.2f} "
                f"x {produto.quantidade} = R$ {produto.subtotal():.2f}"
            )

        print(f"Subtotal: R$ {self.calcular_total():.2f}")
        print(f"Desconto: {self.desconto}%")
        print(f"Valor total: R$ {self.calcular_total_com_desconto():.2f}")