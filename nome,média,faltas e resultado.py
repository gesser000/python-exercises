valid_nota1 = False
valid_nota2 = False
valid_faltas = False
nome = input('digite seu nome: ')

while valid_nota1 == False:
    nota1 = float(input('digite a nota 1: '))
    if nota1 < 0 or nota1 > 10:
        print('A nota precisa estar entre 0 e 10')
        nota1 = float(input('digite nota 1: '))
    else:
        valid_nota1 = True

while valid_nota2 == False:
    nota2 = float(input('digite a nota 2: '))
    if nota2 < 0 or nota2 > 10:
        print('A nota precisa estar entre 0 e 10')
        nota2 = float(input('digite a nota 2: '))
    else:
        valid_nota2 = True
        
while valid_faltas == False:
    faltas = float(input('digite o total de faltas: '))
    if faltas < 0 or faltas > 20:
        print('As faltas precisam estar entre 0 e 20: ')
        faltas = float(input('digite o total de faltas: '))
    else:
        valid_nota = True
        
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
    
    
             
