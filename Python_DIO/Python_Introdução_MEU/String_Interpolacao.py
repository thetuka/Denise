# a interpolação é a utilização da variável no print

# OLD STYLE %
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no surso de %s." % (nome, idade, profissao, linguagem))


# MÉTODO FORMAT
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no surso de {}." .format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no surso de {0}." .format(linguagem, profissao, idade, nome))
    # nesse, podemos informar o indice que está a variavel que desejamos. Muito útil quando a variavel
    # aparece muitas vezes

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no surso de {linguagem}." .format(nome=nome, idade=idade, profissao= profissao, linguagem=linguagem))
    # mesma utilide do de cima, porém aqui, ao invez de passar numeros, passo direto o nome da váriavel e sua atribuição, podendo ser usado
    # diversas vezes sem ter que ficar declarando todas as vezes, ou seja, posso reaproveitar a variavel

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no surso de {linguagem}." .format(**pessoa))
    # nesse usamos um dicionário com todos os requisitos já "pré programados" (será visto mais pra frente)


# MÉTODO F-STRING
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no surso de {linguagem}.")
    # mais usado ultimamente, pois não há necessidade de ficar informando as variáveis

PI = 3.14159
print(f"Valor de PI: {PI:.2f}")
    # se não colocar nada na frente do .2, não vai aparecer "espaços em branco"

print(f"Valor de PI: {PI:10.2f}")
    # aqui, já coloquei 10 na frente, então ele vai considerar 10 espaços antes do decimal