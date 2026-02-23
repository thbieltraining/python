"# Vamos brincar com algumas funções matemáticas em Python!"

"average(10, 20, 30)"
"print(average(10, 20, 30))"
# Eu já sabia que average só recebe 2 argumentos, mas eu queria testar kkkk
"average(10, 20)"
"print(average(10, 20))"
# Joguei as primeiras average entre aspas só para não ficar um limbo de argumentos no comentário.
# Falou que não tá definido, porquê será ?
"Como fazer a função average funcionar ?"


def average(a, b):
    return (a + b) / 2


a = 10
b = 20
# Tá, agora a função average está definida, vamos testar de novo, mas ta diferente do livro
print(average(a, b))
# Chat, por que a função average não foi aceita igual tava no meu livro ?
"""
Calcula a média aritmética de dois números.
Args:
    a (int or float): Primeiro número
    b (int or float): Segundo número
Returns:
    float: A média aritmética entre a e b
Example:
    >>> average(10, 20)
    15.0
Note:
    A função foi definida DEPOIS das primeiras tentativas de uso.
    Por isso dava erro "não está definido" - Python precisa conhecer a função
    ANTES de você tentar usá-la. A ordem de execução importa!
    Se você chamar a função antes da definição (def), Python lança NameError.
"""
" Entendiiiiiiiiiiiiiiiiiiiiiii, faz total sentido mesmo "
