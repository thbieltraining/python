import math

"Vou começar com um def direto já"

a = 1


def perimeter(a):
    return a


print(perimeter(a))


# Tá, isso não é um perímetro, mas é um começo, vamos tentar de novo
def perimeter(a):
    return 4 * a


print(perimeter(a))
# Agora sim, isso é um perímetro de um quadrado, mas e se eu quiser o perímetro de um circulo ?
"Eu tava esquecendo de usar a biblioteca math"
"#import math"

perimeter(1)
print(perimeter(1))
# Tá, isso não parece o perímetro de um círculo de raio 1
" Explica pra nós ai chat o que tá acontecendo ? "
"""
Calcula o perímetro de um quadrado dado o comprimento de um lado.
A função atual retorna 4 * a, que é o perímetro de um quadrado.
Para calcular o perímetro de um círculo (circunferência), você precisa usar:
circumference = 2 * π * r, onde r é o raio.
A função perimeter() está retornando o perímetro do quadrado corretamente (4 * a),
mas NÃO está calculando a circunferência de um círculo.
Para um círculo com raio 1, a circunferência deveria ser:
2 * π * 1 ≈ 6.28, mas a função está retornando 4 (que é 4 * 1).
Se você quer uma função que calcule o perímetro de um círculo, precisa modificá-la:
    return 2 * math.pi * a
Args:
    a: Comprimento do lado (quadrado) ou raio (círculo)
Returns:
    float: O perímetro/circunferência calculado
"""
" Vamos tentar então"


def perimeter(a):
    return 2 * math.pi * a


a = 1
print(perimeter(a))
# Agora sim, isso é o perímetro de um círculo de raio 1, uhuuuu
"#Aqui tomei xingo do terminal, porque não usei a hierarquia do código, mas agora entendi que a função tem que ser definida antes de ser chamada, e não depois, como eu fiz no começo, mas tudo bem, faz parte do processo de aprendizado"
