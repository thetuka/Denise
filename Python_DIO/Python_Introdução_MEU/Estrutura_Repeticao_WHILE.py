#utilizado para repetir várias vezes, qdo não sabemos quantas vezes ele vai ser executado

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n:"))
    
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigada por usar nossos serviços!!! :) ")