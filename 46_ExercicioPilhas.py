"Vamos implementar um código que realiza a conversão de um número decimal para binário usando uma pilha. A ideia é dividir o número decimal por 2 repetidamente e armazenar os restos em uma pilha. Depois, ao desempilhar os restos, obtemos a representação binária do número."


class Pilha:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()
        else:
            raise IndexError("A pilha está vazia")

    def peek(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            raise IndexError("A pilha está vazia")

    def isEmpty(self):
        return len(self.data) == 0


Pilha = Pilha()
num = 10  # Número decimal a ser convertido
while num > 0:
    resto = num % 2
    Pilha.push(resto)
    num = num // 2
while not Pilha.isEmpty():
    print(
        Pilha.pop(), end=""
    )  # Imprime os restos desempilhados para formar o número binário
# Output: 1010 (que é a representação binária de 10)
