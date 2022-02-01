vendas = []
comprar = 's'
total = 0
valid_valor = False

while comprar == 's' :
    item = input('insira o item: ')

    while valid_valor == False:
        valor = input('insira o valor: ')
        try:
            valor = float(valor)

            if valor < 0:
                print('o preço pecisa ser positivo')
            else:
                valid_valor = True
        except:
            print("formato de preço inválido. Use apenas preços e separe os centavos com "'.')

    vendas.append(item)
    vendas.append(valor)
    total = total + valor
    valid_valor = False
    comprar = input('quer continuar comprado ? ')
    


print('a sua lista de compras foi:',vendas)
print ('o total de sua compra foi:',total)
