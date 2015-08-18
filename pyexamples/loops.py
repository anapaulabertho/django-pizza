pedidos = [
    {
        'nome': 'Mario',
        'sabor': 'Portuguesa'
    },
    {
        'nome': 'Marco',
        'sabor': 'Presunto'
    }
]

for pedido in pedidos:
    print ('Nome: {0}\nSabor: {1}'.format(pedido['nome'], pedido['sabor']))
