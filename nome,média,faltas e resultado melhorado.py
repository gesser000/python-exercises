valid_nota1 = False
valid_nota2= False
valid_falta = False
nome = input('digite seu nome: ')

while valid_nota1 == False:
    nota1 = input('digite a nota 1: ')
    try:
        nota1= float(nota1)

        if nota1 < 0 or nota1 > 10:
            print('a nota precisa estar entre 0 e 10')
        else:
            valid_nota1 = True

while valid_nota2 == False:
    nota2 = input('digite a nota 1: ')
    try:
        nota2= float(nota1)

        if nota2 < 0 or nota2 > 10:
            print('a nota precisa estar entre 0 e 10')
        else:
            valid_nota2 = True
            
faltas = int(input('digite o total de faltas: '))

média = (nota1 + nota2)/2
faltasper = faltas/20
 

print('nome do aluno: ',nome)
print('a sua média é: ',média)
print('o seu percentual de faltas é: ',faltasper)
if média < 6 and faltasper >= 0.7:
    print('reprovado por notas e faltas')

elif média < 6 and faltasper <= 0.6:
    print('reprovado por notas')

elif média > 6 and faltasper >= 0.7:
    print('reprovado por faltas')

else:
    print('aprovado')
    
    
             
