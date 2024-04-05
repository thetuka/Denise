#Receba um numrto e exiba 2 numeros seguintes 
# comando FOR
## o for é bem executado, quando sabemos a quantia exata da repetição

a = int(input("Informe um numero: "))
print(a)

a += 1
print(a)

a += 1
print(a)

#texto = input("Informe um texto: ")
texto = ""
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end=" ")
else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")