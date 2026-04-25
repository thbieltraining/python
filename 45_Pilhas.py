"Vamo falar de pilhas em python ? Vamos lá !"

"Uma pilha é uma estrutura de dados que segue o princípio LIFO (Last In, First Out), ou seja, o último elemento adicionado é o primeiro a ser removido."
"Tambem é bom lembrar que não podemos tirar a pilha do lugar, ou seja, só podemos acessar o topo da pilha."

"Algumas funções comuns em uma pilha incluem: push (adicionar um elemento), pop (remover o elemento do topo), peek (ver o elemento do topo sem removê-lo) e isEmpty (verificar se a pilha está vazia)."

" Em Python, podemos implementar uma pilha usando uma lista. Aqui está um exemplo simples de como criar e usar uma pilha em Python:"


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


# Exemplo de uso

pilha = Pilha()
pilha.push(1)
pilha.push(2)
print(pilha.peek())
pilha.pop()  # Output: 2
print(pilha.peek())  # Output: 1
# Aqui o ultimo elemento adicionado foi o 2, então ele é o primeiro a ser removido. Depois disso, o topo da pilha é o 1.
