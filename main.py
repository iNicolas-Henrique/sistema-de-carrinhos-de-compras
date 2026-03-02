import os
import random
from produto import Produto
from carrinho import Carrinho

# Limpa a tela do terminal pra não ficar muito poluido
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Gera lista inicial de produtos com preço e estoque aleatórios pois acredito que seja melhor assim.
def gerar_produtos():
    nomes = [
        "Arroz", "Sopa", "Macarrão", "Carne",
        "Frango", "Leite", "Ovos", "Pão",
        "Queijo", "Maçã"
    ]

    lista = []

    for nome in nomes:
        preco = round(random.uniform(2, 15), 2)
        estoque = random.randint(20, 150)

        lista.append({
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        })

    return lista

# Mostra os produtos disponíveis no estoque
def mostrar_produtos(produtos):
    print("Produtos disponiveis:\n")

    for i, p in enumerate(produtos):
        print(
            f"{i+1} - {p['nome']} | "
            f"R$ {p['preco']:.2f} | "
            f"Estoque: {p['estoque']}"
        )

# Exibe o menu principal
def menu():
    print("\n1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Ver carrinho")
    print("4 - Confirmar compra")
    print("0 - Sair")

# Função principal do sistema
def main():
    carrinho = Carrinho()       # Cria o carrinho
    produtos = gerar_produtos() # Gera produtos iniciais

    while True:
        limpar_tela()
        menu()
        opcao = input("Escolha: ")

        limpar_tela()

        if opcao == "1":
            mostrar_produtos(produtos)

            try:
                escolha = int(input("\nNumero do produto: ")) - 1

                if escolha < 0 or escolha >= len(produtos):
                    print("Produto invalido.")
                else:
                    produto_escolhido = produtos[escolha]
                    qtd = int(input("Quantidade: "))

                    if qtd <= 0:
                        print("Quantidade invalida.")
                    elif qtd > produto_escolhido["estoque"]:
                        print("Nao tem essa quantidade em estoque.")
                    else:
                        # Cria objeto Produto e adiciona ao carrinho
                        novo = Produto(
                            produto_escolhido["nome"],
                            produto_escolhido["preco"],
                            qtd
                        )

                        carrinho.adicionar_produto(novo)
                        produto_escolhido["estoque"] -= qtd

                        print("Produto adicionado.")

            except ValueError:
                print("Entrada invalida.")
#
        elif opcao == "2":
            carrinho.remover_produto(produtos)

        elif opcao == "3":
            carrinho.listar_produtos()

        elif opcao == "4":
            if not carrinho.produtos:
                print("Carrinho vazio.")
            else:
                carrinho.aplicar_desconto()
                carrinho.gerar_nota_fiscal()
                print("Compra finalizada.")
                carrinho = Carrinho()

        elif opcao == "0":
            break

        else:
            print("Não é possivel fazer tal operação.")

        input("\nPressione ENTER para retorna ao menu principal...")

# Garante que o programa só execute se for rodado diretamente
if __name__ == "__main__":

    main()
