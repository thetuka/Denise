#o break para o laço de repetição se a condição for atendida
# geralmente usado com while, mas pode ser usado também com o for

while True:
    numero = int(input("Informe um numero:"))
    
    if numero == 10:
        break # quando quer cortar a execução
    
    if numero % 2 == 0:
        continue # nesse caso, ele pula uma execução
    
    print(numero)
    
# for numero in range(100):
#     if numero == 12:
#         #break  # quando quer cortar a execução
#         continue # nesse caso, ele pula uma execução
    
#     print(numero, end=" ")