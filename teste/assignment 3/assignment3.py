# Importando biblioteca para utilizar arquivos JSON
import json

# Abrindo o diretório do arquivo JSON
f = open('dados.json')

# Carregando os dados do arquivo JSON e salvando num dicionário
dados = json.load(f)

# Declarando variáveis
aux = 0
maior = 0
menor = 0
soma = 0
media = 0


for dia in dados:

    # Considerando apenas os casos onde o valor de faturamento não é zero.
    if (dia['valor']) != 0:
        aux = dia['valor']

        # Calculando o maior faturamento
        if (aux > maior):
            maior = aux

        # Calculando o menor faturamento
        if(menor == 0):
            menor = aux
        elif (aux < menor):
            menor = aux

        # Somando os valores de faturamento
        soma += dia['valor']

print('O maior valor de faturamento do mes foi: R$ ' + str(maior) + '.')
print('O menor valor de faturamento do mes foi: R$ ' + str(menor) + '.')


# Dividindo a soma pelo número de dias para obter a média
media = soma / len(dados)

# Criando variável para armazenar os dias que o faturamento foi acima da média
diasFaturamento = ''

for i in dados:
    if (i['valor']) != 0:
        # Caso o valor do faturamento do dia for maior que a média, salva o número do dia na String
        if (i['valor']) > media:
           diasFaturamento += (str(i['dia']) + ' ')
        
print('Os dias em que o faturamento foi maior que a media mensal foram: ' + diasFaturamento)