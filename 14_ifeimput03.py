"Aqui vou criar um código que recebe um input do usuario e tenta converter para respectivos lados de um possível triângulo"

a = eval(input("Digite o valor do lado A: "))
b = eval(input("Digite o valor do lado B: "))
c = eval(input("Digite o valor do lado C: "))
maior_lado = 0
if a > b and a > c:
    maior_lado = a
elif b > a and b > c:
    maior_lado = b
else:
    maior_lado = c
if maior_lado < a + b + c - maior_lado:
    "Chat o terminal ta bugando no meu -, pq isso ta acontecendo ?"
    print("É possível formar um triângulo com os lados informados.")
else:
    print("Não é possível formar um triângulo com os lados informados.")

if a == b and b == c and a == c:
    print("O triângulo é equilátero.")
elif a != b and b != c and a != c:
    print("O triângulo é escaleno.")
else:
    print("O triângulo é isósceles.")
