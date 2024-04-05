def sacar(valor: float):
    saldo = 500
    
    if saldo >= valor:
        print("valor sacado!")
        print("Retire seu dinheiro na boca do caixa!")
        
    print("Obrigada por ser nosso cliente, tenha um bom dia!")
        
def depositar(valor):
    saldo = 500
    saldo += valor

depositar(20)     
sacar(1000)
