meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
nasc = input ('insira sua data de aniversário no formato DD-MM-AAAA: ')

indice = int (nasc[3:5])-1
mes = meses[indice]

print ('você nsceu no mês:',mes)

