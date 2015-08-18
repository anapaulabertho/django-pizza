pedidos = []


# def nome_da_funcao(): declarar uma funcao
def criar_pedido(nome, sabor, observacao=None):
    pedido = {}  # cria um dicionario vazio
    pedido['nome'] = nome  # chave para o dicionario
    pedido['sabor'] = sabor  # chave para o dicionario
    pedido['observacao'] = observacao
    return pedido

pedidos.append(criar_pedido('mario', 'pepperoni'))
pedidos.append(criar_pedido('marco', 'presunto', 'xyz'))

for pedido in pedidos:
    template = 'Nome: {nome}\nSabor: {sabor}'
    print(template.format(**pedido))  # ** significa que passa cada argumento
# do dicionario como argumento da funcao
    if pedido['observacao']:
        print('Observacao: {}'.format(pedido['observacao']))

    print('-'*20)
