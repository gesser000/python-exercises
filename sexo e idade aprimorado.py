idade = int(input('Digite sua idade: '))
sexo = input('Digite seu sexo: ').lower()
cidade = input('Digite sua cidade: ').lower()

if cidade == 'palhoça' or cidade == 'são josé':

    if sexo == 'masculino':
        if idade <18:
            print('Homem menor de idade, da grande florianópolis')
        else:
            print('Homem maior de idade, da grande florianópolis')

    elif sexo == 'feminino':
        if idade <18:
            print('Mulher menor de idade, da grande florianópolis')
        else:
            print('Mulher maior de idade, da grande florianópolis')

    else:
        print('Erro na entrada de dados, da grande florianópolis')

else:
    print('teste apenas para pessoas da grande florianópolis')
