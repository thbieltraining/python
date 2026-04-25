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


# Criando as duas filas
fila_prioritaria = Fila()
fila_normal = Fila()

# Inserindo pessoas (nome, idade)
pessoas = [
    ("Ana", 65),
    ("João", 30),
    ("Maria", 72),
    ("Carlos", 45),
    ("Dona Rosa", 80),
    ("Pedro", 25),
]

for nome, idade in pessoas:
    if idade > 60:
        fila_prioritaria.enqueue((nome, idade))
        print(f"{nome} ({idade} anos) -> fila PRIORITÁRIA")
    else:
        fila_normal.enqueue((nome, idade))
        print(f"{nome} ({idade} anos) -> fila NORMAL")

print("\n--- Atendimento ---")

# A cada 2 da prioritária, 1 da normal
prioritaria_count = 0

while not fila_prioritaria.isEmpty() or not fila_normal.isEmpty():
    # Atende da prioritária
    if not fila_prioritaria.isEmpty():
        pessoa = fila_prioritaria.dequeue()
        print(f"Atendendo (prioritária): {pessoa[0]}")
        prioritaria_count += 1

        # A cada 2 da prioritária, atende 1 da normal
        if prioritaria_count % 2 == 0 and not fila_normal.isEmpty():
            pessoa_normal = fila_normal.dequeue()
            print(f"Atendendo (normal):      {pessoa_normal[0]}")
    else:
        # Prioritária vazia, esvazia a normal
        pessoa = fila_normal.dequeue()
        print(f"Atendendo (normal):      {pessoa[0]}")
