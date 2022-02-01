idade = int(input('Digite sua idade: '))
sexo = input('Digite seu sexo: ').lower()

if idade < 18 and sexo == 'masculino':
    print('homem menor de idade')

elif idade >= 18 and sexo == 'masculino':
    print('homem maior de idade')

elif idade < 18 and sexo == 'feminino':
    print('mulher menor de idade')

elif idade >= 18 and sexo == 'feminino':
    print('mulher maior de idade')

else:
    print('erro na entrada')
