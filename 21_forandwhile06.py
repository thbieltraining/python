def fat(b):
    n = 0  # Inicializa o contador em 0
    fat = 1  # Inicializa o resultado (fatorial) em 1
    while n <= b:  # Enquanto n for menor ou igual ao parâmetro b
        n += 1  # Incrementa n em 1
        fat *= n  # Multiplica o resultado por n
    return fat  # Retorna o fatorial de b


print(fat(3))
