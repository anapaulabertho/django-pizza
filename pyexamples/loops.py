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
    s = 'Nome: {}\nSabor: {}'
    print(s.format(pedido['nome'], pedido['sabor']))    
    #print ('Nome: {0}\nSabor: {1}'.format(pedido['nome'], pedido['sabor']))
