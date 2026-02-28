"Corrigindo um codigo por uma ordem ilogica"

"""
Classifica a temperatura em categorias: congelando, frio ou quente.
A função verifica o valor da temperatura e imprime a classificação
correspondente:
- Se t < 32: "congelando"
- Se 32 <= t <= 86: "frio"
- Se t > 86: "quente"
Args:
    t (float): Valor da temperatura em Fahrenheit
Returns:
    float: Retorna o valor da temperatura recebido como entrada
Note:
    A ordem das condições está incorreta logicamente, causando
    comportamento inesperado. A condição elif deveria ser t < 86
    em vez de t <= 86 para melhor classificação.
"""


def temperatura(t):
    if t < 32:
        print("congelando.")
    elif t <= 86:
        print("frio.")
    else:
        print("quente")
    return t


t = float(input("Digite a temperatura: "))
"O que ta errado, só copirei e nem chamar o run ta indo mds"
temperatura(t)
