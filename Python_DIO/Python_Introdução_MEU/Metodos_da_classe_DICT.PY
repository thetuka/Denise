#### {}.clear
# apaga os valores do dicionário, quando quero apagar TUDO

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "333-123"},
    "giovana@gmail.com": {"nome": "Giovana", "telefone": "333-321"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "333-132"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "333-213", "extra": {"a":1}},
}

contatos.clear()
print(contatos)


#### {}.COPY
# copia os dados. Usado qdo quero mudar os dados, mas não alterar

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "333-123"},
}

#### {}.FROMKEYS
# usado para adicionar novas chaver para o dicionario, sem preencher 
# as informaçõs, tipo  ypsly lipsy



#### {}.GET
# é uma segunda forma de acessar os dados do dicionário

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "333-123"},
}

contatos["chave"] # KeyError --- faz o programa parar

contatos.get("chave")
contatos.get("chave", {}) # as {} é qdo não tem retorno, vazio, nulo
contatos.get("guilherme@gmail.com", {})

#### {}.ITEMS
# retona lista de tuplas

#### {}.KEYS
# retorna só uma chave do dicionário

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "333-123"},
}

resultado = contatos.keys()
print(resultado)

novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.keys())


#### {}.POP
# remove a chave do dicionario

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "333-123"},
}

contatos.pop("guilherme@gmail.com")
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", "não encontrou") # aqui foi usado o argumento, caso não ache a chave


#### {}.POPITEM
# aqui não informa a chave, ele vai retirando 1 por 1


#### {}.SETDEFAULT
# se o atributo não estiver no dicionário, ele adiciona. 
# Se o atributo estiver, ele retorna o valor e não altera


#### {}.UPDATE
# ele deixa eu atualizar meu dicionario com um novo dicionario


#### {}.VALUES
# retorna apenas os valores do dicionario, sem as chaves


#### IN
# metodo de verificação de forma mais fácil


#### DEL
# outra forma de tirar o valor. Passando o objeto que quero remover