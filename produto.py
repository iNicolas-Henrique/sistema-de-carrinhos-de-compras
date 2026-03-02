# Classe responsável por representar um produto dentro do sistema
class Produto:
    def __init__(self, nome, preco, quantidade):
        # Atributos principais do produto
        self.nome = nome              # Nome do produto
        self.preco = preco            # Preço unitário
        self.quantidade = quantidade  # Quantidade adicionada ao carrinho

    # Método que calcula o valor total daquele produto
    # (preço unitário multiplicado pela quantidade)
    def subtotal(self):
        return self.preco * self.quantidade