pedidos = []


# def nome_da_funcao(): declarar uma funcao
def adiciona_pedido(nome, sabor):
    pedido = {}  # cria um dicionario vazio
    pedido['nome'] = nome  # chave para o dicionario
    pedido['sabor'] = sabor  # chave para o dicionario

    pedidos.append(pedido)  # add a variavel pedido ao final da lista

print(pedidos)

adiciona_pedido('mario', 'pepperoni')
adiciona_pedido('marco', 'presunto')

print(pedidos)