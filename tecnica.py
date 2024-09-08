#Cálculo da variável SOMA no trecho de código
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(f"Valor da SOMA: {SOMA}")

# Verificação se um número pertence à sequência de Fibonacci
def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Entrada do usuário ou valor pré-definido
num = int(input("Informe um número: "))

if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")

#Faturamento diário de uma distribuidora
import json

# Exemplo de dados de faturamento diário em JSON
faturamento_json = '''
{
    "faturamento_diario": [1000, 0, 1200, 0, 800, 3000, 0, 900, 0, 0, 500, 1000, 0, 750, 2000]
}
'''

# Carregar os dados JSON
faturamento = json.loads(faturamento_json)["faturamento_diario"]

# Remover dias sem faturamento (valores iguais a 0)
faturamento_filtrado = [valor for valor in faturamento if valor > 0]

# Calcular menor e maior valor
menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)

# Calcular a média mensal
media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

# Contar quantos dias tiveram faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

# Percentual de representação do faturamento por estado
def calcular_percentual_faturamento():
    # Valores de faturamento por estado
    sp = 67836.43
    rj = 36678.66
    mg = 29229.88
    es = 27165.48
    outros = 19849.53

    # Calcular o total
    total = sp + rj + mg + es + outros

    # Calcular e exibir os percentuais
    print(f"Percentual SP: {sp / total * 100:.2f}%")
    print(f"Percentual RJ: {rj / total * 100:.2f}%")
    print(f"Percentual MG: {mg / total * 100:.2f}%")
    print(f"Percentual ES: {es / total * 100:.2f}%")
    print(f"Percentual Outros: {outros / total * 100:.2f}%")

# Chamar a função para executar o cálculo
calcular_percentual_faturamento()

# Programa que inverte os caracteres de uma string
def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# Entrada do usuário ou string definida no código
texto = input("Digite uma string: ")

print(f"String invertida: {inverter_string(texto)}")