Maior_idade = 18
Idade_especial = 17

idade = int(input("Informe sua idade: "))

if idade >= Maior_idade:
    print("Maior de idade, pode tirar a CNH")
if idade < Maior_idade:
    print("Não pode tirar ainda")
    
if idade >= Maior_idade:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Não pode tirar ainda")


if idade >= Maior_idade:
    print("Maior de idade, pode tirar a CNH")
elif idade == Idade_especial:
    print("Pode fazer teórica, mas não pode fazer aulas práticas")
else:
    print("Ainda não pode tirar CNH")
    
