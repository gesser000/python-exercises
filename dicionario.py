colors = {'vermelho' : 'red','azul' : 'blue','verde' : 'green'}
cor = input ('escreva uma cor: ').lower()
tradução = colors.get (cor, 'esta cor nao consta no dicionario')
print (tradução)
