curso = "pYtHon"

print(curso.upper()) #converte para maiusculo
print(curso.lower()) #converte em minusculo
print(curso.title()) #deixa apenas a 1 maiuscula

curso = "      pYtHon   "

print(curso.strip()) # retira o espaço do começo e fim
print(curso.lstrip()) # remove o espaço do lado esquerdo
print(curso.rstrip()) # remove o espaço do lado direito

curso = "Python"

print(curso.center(10)) # centraliza o texto, usando o total de espaços informados (espaço + valor)
print(curso.center(10, "#")) # texto centralizado, com caracteres adicionais, 
#sendo o total de 10 caracteres com a junção da variavel e do caractere #
print(".".join(curso)) # junção, no exemplo, estamos juntando o ponto (.) entre as letras. 
#JOIN pode ser usado com todo iteravel
