"Já para calcular o fatorial de um número usando iteração, podemos usar um loop for ou while. Por exemplo:"


def fat_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


print(fat_iterativo(5))
"Ambos os códigos calculam o fatorial de 5, mas um usa recursão e o outro usa iteração. A escolha entre recursão e iteração depende do problema que estamos tentando resolver e das preferências pessoais do programador. Em geral, a recursão pode ser mais elegante e fácil de entender para problemas que têm uma estrutura recursiva natural, enquanto a iteração pode ser mais eficiente em termos de tempo de execução e uso de memória para problemas que não têm uma estrutura recursiva clara."
