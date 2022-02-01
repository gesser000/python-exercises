x = 0
pessoas = []

while x < 4:
    nome = input ('Qual seu nome ?')
    if nome == 'joão':
        break
    pessoas.append(nome)
    x = x + 1
    

print(pessoas)
