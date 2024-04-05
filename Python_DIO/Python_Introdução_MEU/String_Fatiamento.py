# tecnica para retornar substring, informando inicio(start), fim(stop) e passo(step)= [start: stop[,step]]


nome = "Guilherme Arthur de Carvalho"

print(nome[0]) # aqui ele paga o indice
print(nome[:9]) # se não colocar o inicio, ele pega desde o indice 0 e vai até o stop, aqui, 9
print(nome[10:]) # se eu não informar o stop, ele começa a contar do 10 e vai até o final da string
print(nome[10:16]) # inicio e fim da strin, inicio no indice 10 e fim 16
print(nome[10:16:2]) # inicio e fim da string, com a contagem de passada
print(nome[:]) # traz a string inteira
print(nome[:: -1]) #espelhamento da string