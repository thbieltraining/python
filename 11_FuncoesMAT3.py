import math

"Antes de começar quero enteder a diferença entre average e média, e também a diferença entre median e mediana."

"Claro! Vamos esclarecer as diferenças entre esses termos:"
"1. **Average (Média)**: A média é a soma de um conjunto de números dividida pelo número total de elementos nesse conjunto. Por exemplo, a média de 2, 3 e 5 é (2 + 3 + 5) / 3 = 10 / 3 ≈ 3.33."
"2. **Median (Mediana)**: A mediana é o valor que separa a metade superior da metade inferior de um conjunto de dados ordenados. Se o número de elementos for ímpar, a mediana é o valor do meio. Se for par, a mediana é a média dos dois valores centrais. Por exemplo, para os números 2, 3 e 5, a mediana é 3 (o valor do meio). Para os números 2, 3, 5 e 7, a mediana é (3 + 5) / 2 = 4."

"No caso eu queia testar a diferença da função average e média, e também a diferença entre median e mediana usando o código abaixo:"


"average = 1, 2, 3"
"average(1, 2, 3)"
"print(average)"
"Não entnedi"
"#Explica por favor chat, o que tá acontecendo ?"
"""
"O código que você escreveu tem um erro de sintaxe. Quando você faz `average = 1, 2, 3`, você está criando uma tupla com os valores (1, 2, 3) e atribuindo essa tupla à variável `average`. Isso significa que `average` agora é uma tupla, e não uma função."
"""
"Quando você tenta chamar `average(1, 2, 3)`, Python tenta executar a tupla como se fosse uma função, o que resulta em um erro de tipo (TypeError), porque uma tupla não é chamável."

"Para corrigir isso, você precisa definir `average` como uma função usando `def`, e não atribuir uma tupla a ela. Por exemplo:"


def average(*numbers):
    return sum(numbers) / len(numbers)


# E agora ?
print(average(1, 2, 3))


def media(*numbers):
    return sum(numbers) / len(numbers)


print(media(1, 2, 3))

"#Chat me explica o que é o sum e o len dnetro de def pfv"
"O `sum(numbers)` calcula a soma de todos os números passados como argumentos para a função."
"O `len(numbers)` retorna o número de elementos na tupla `numbers`."
"Assim, a função `average` calcula a média dos números passados como argumentos."
"Mas então qual a diferença entre average e media ?"
"Em Python, `average` e `media` são apenas nomes diferentes para a mesma função. Ambas calculam a média aritmética de um conjunto de números. O nome `average` é mais comum em contextos de programação em inglês, enquanto `media` é uma tradução direta do termo em português."
# WOW, incrivel !!
# Pq ta dizendo que eu não usei import math chat ?
# A função perimeter NÃO é do math. Você precisa criar ela customizada.
# O math tem funções como sqrt, pi, sin, cos, etc.


# Exemplo de função perimeter (perímetro):
def perimeter_circle(radius):
    return 2 * math.pi * radius


def perimeter_square(side):
    return 4 * side


def perimeter_rectangle(length, width):
    return 2 * (length + width)


# Exemplos de funções do math:
print(math.sqrt(16))  # Raiz quadrada: 4.0
print(math.pi)  # Pi: 3.14159...
print(math.sin(math.pi / 2))  # Seno: 1.0
print(math.cos(0))  # Cosseno: 1.0
print(math.floor(3.9))  # Arredonda p/ baixo: 3
print(math.ceil(3.1))  # Arredonda p/ cima: 4

# Testando seus perímetros:
print(perimeter_circle(5))  # Perímetro do círculo
print(perimeter_square(4))  # Perímetro do quadrado
print(perimeter_rectangle(5, 3))  # Perímetro do retângulo
"Entendi  melhor agora, mas então tá diferente do livro..."
