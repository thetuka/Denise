# um diciionario é um conjunto não ordenado de pares chave: valor, 
# onde as chaves são unicas em uma dada instancia do dicionário
# para criar um dicionário, a gente usa {}

pessoa = {"nome": "Guilherme", "idade": 28} #essa é uma forma

pessoa = dict(nome="Guilherme", idade= 28) #outra forma de criar dicionario

pessoa["telefone"] = "333-123" #qdo já tenho um dicionário e estou adicionando 
#uma chave nova, aqui, é telefone
print(pessoa)

# EXEMPLO
dados = {"nome": "Guilherme", "idade": 28, "telefone": "333-123"}
#dicionário criado acima

dados["nome"]
dados["idade"]
dados["telefone"]
# aqui eu estou 'chamando' os dados do dicionário
print(dados)


dados["nome"] = "Maria"
dados["idade"] = 25
dados["telefone"] = "444-321"
# aqui eu estou alterando o valor do dicionario

print(dados)  # {"nome": "Maria", "idade": 25, "telefone": "444-321"}
# aqui seria como ficou o dicionario após a alteração