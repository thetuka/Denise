# Dicionarios podem armazenas qq tipo de objeto no Python como valor
# desde quea chave para esse valor seja um objeto imutável como string ou numeros

#EXEMPLO
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "333-123"},
    "giovana@gmail.com": {"nome": "Giovana", "telefone": "333-321"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "333-132"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "333-213", "extra": {"a":1}},
}

telefone = contatos["giovana@gmail.com"]["telefone"]
print(telefone)

extra = contatos["melaine@gmail.com"]["extra"]["a"]
print(extra)


##### ITERAR DICIONÁRIO
#para iterar, usamos o for

for chave in contatos:
    print(chave, contatos[chave])
# esse é um jeito de chamar
    
for chave, valor in contatos.items():
    print(chave, valor)
# esse é outro jeito