"Vamos falar de filas em python ? Vamos lá !"

"Uma fila é uma estrutura de dados que segue o princípio FIFO (First In, First Out),parece aquilo de estoque, quem trabalhou em lojas deve saber... basicamente, o primeiro elemento adicionado é o primeiro a ser removido."
"Tambem é bom lembrar que não podemos tirar a fila do lugar, ou seja, só podemos acessar o início e o final da fila."

"Algumas funções comuns em uma fila incluem: enqueue (adicionar um elemento), dequeue (remover o elemento do início), front (ver o elemento do início sem removê-lo) e isEmpty (verificar se a fila está vazia)."

"Diferença entre pilha e fila: A pilha segue o princípio LIFO, onde o último elemento adicionado é o primeiro a ser removido, enquanto a fila segue o princípio FIFO, onde o primeiro elemento adicionado é o primeiro a ser removido."

" Em Python, podemos implementar uma fila usando uma lista. Aqui está um exemplo simples de como criar e usar uma fila em Python:"


class Fila:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.data.pop(0)
        else:
            raise IndexError("A fila está vazia")

    def front(self):
        if not self.isEmpty():
            return self.data[0]
        else:
            raise IndexError("A fila está vazia")

    def isEmpty(self):
        return len(self.data) == 0


# Exemplo de uso

fila = Fila()
fila.enqueue(1)
fila.enqueue(2)
print(fila.front())
fila.dequeue()  # Output: 1
print(fila.front())  # Output: 2
# Aqui o primeiro elemento adicionado foi o 1, então ele é o primeiro a ser removido. Depois disso, o início da fila é o 2.
"Ele não foi removido no terminal porque ? "
"Porque o método dequeue() remove o elemento do início da fila, mas não o imprime. Se quisermos ver o elemento removido, podemos armazená-lo em uma variável e imprimi-lo, assim:"
removido = fila.dequeue()
print(removido)  # Output: 2
# Agora sim, o elemento removido (2) é impresso no terminal.
"Mas afinal, qual a vantagem de usar uma fila em vez de uma lista comum ?"
"Usar uma fila pode ser vantajoso quando precisamos garantir a ordem de processamento dos elementos, como em situações de atendimento ao cliente, gerenciamento de tarefas ou simulações. As filas permitem que os elementos sejam processados na ordem em que foram adicionados, o que pode ser crucial para manter a integridade dos dados e garantir um fluxo de trabalho eficiente."
"Qual seria um exemplo prático de uso de filas ?"
"Um exemplo prático de uso de filas é em um sistema de atendimento ao cliente, onde os clientes chegam e são atendidos na ordem em que chegaram. Cada cliente é adicionado à fila de atendimento, e o atendente processa os clientes um por um, garantindo que o primeiro cliente a chegar seja o primeiro a ser atendido. Isso ajuda a manter a organização e a eficiência no atendimento ao cliente."
"Em uma aplicação pode dizer que seria como os  tickets para atendimento, onde cada cliente recebe um número e é atendido na ordem dos números, garantindo que o processo seja justo e eficiente."
