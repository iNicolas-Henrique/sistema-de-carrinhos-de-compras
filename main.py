import os
import random
from produto import Produto
from carrinho import Carrinho


# Limpa a tela para não acumular informação antiga e torna menos poluido.
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


# Gera uma lista inicial de produtos com preço e estoque aleatórios
# Fiz assim para o sistema não ficar sempre com os mesmos valores
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

        # Aqui eu guardo as informações de cada produto em formato de dicionário
        lista.append({
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        })

    return lista


# Mostra todos os produtos disponíveis no estoque
def mostrar_produtos(produtos):
    print("Produtos disponíveis:\n")

    for i, p in enumerate(produtos):
        print(
            f"{i+1} - {p['nome']} | "
            f"R$ {p['preco']:.2f} | "
            f"Estoque: {p['estoque']}"
        )


# Menu principal do sistema
def menu():
    print("\n1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Ver carrinho")
    print("4 - Confirmar compra")
    print("0 - Sair")


# Parte responsável por adicionar produto no carrinho
def adicionar_produto(carrinho, produtos):
    mostrar_produtos(produtos)

    # Tenta converter a escolha para número
    try:
        escolha = int(input("\nNúmero do produto: ")) - 1
    except ValueError:
        print("Entrada inválida.")
        return

    # Verifica se o número digitado existe na lista
    if escolha < 0 or escolha >= len(produtos):
        print("Produto inválido.")
        return

    produto_escolhido = produtos[escolha]

    # Agora pede a quantidade
    try:
        qtd = int(input("Quantidade: "))
    except ValueError:
        print("Entrada inválida.")
        return

    # Validações básicas
    if qtd <= 0:
        print("Quantidade inválida.")
        return

    if qtd > produto_escolhido["estoque"]:
        print("Não há essa quantidade em estoque.")
        return

    # Cria o objeto Produto com os dados escolhidos
    novo = Produto(
        produto_escolhido["nome"],
        produto_escolhido["preco"],
        qtd
    )

    # Adiciona no carrinho
    carrinho.adicionar_produto(novo)

    # Atualiza o estoque
    produto_escolhido["estoque"] -= qtd

    print("Produto adicionado.")


# Finaliza compra e gera nota fiscal
def finalizar_compra(carrinho):
    # Se não tiver nada no carrinho, não faz sentido continuar então retorna ao menu.
    if not carrinho.produtos:
        print("Carrinho vazio.")
        return carrinho

    # Aplica desconto (tendo chance de ter ou não)
    carrinho.aplicar_desconto()

    # Gera nota fiscal formatada
    carrinho.gerar_nota_fiscal()

    print("Compra finalizada.")

    # Retorna um novo carrinho vazio
    return Carrinho()


def main():
    # Cria o carrinho principal
    carrinho = Carrinho()

    # Gera os produtos iniciais
    produtos = gerar_produtos()

    while True:
        limpar_tela()
        menu()

        opcao = input("Escolha: ")

        limpar_tela()

        # Usei match case para deixar o menu mais organizado
        match opcao:

            case "1":
                adicionar_produto(carrinho, produtos)

            case "2":
                carrinho.remover_produto(produtos)

            case "3":
                carrinho.listar_produtos()

            case "4":
                carrinho = finalizar_compra(carrinho)

            case "0":
                break

            case _:
                print("Opção inválida.")

        input("\nPressione ENTER para retornar ao menu principal...")


# Isso garante que o programa só roda se esse arquivo for executado diretamente
if __name__ == "__main__":
    main()
