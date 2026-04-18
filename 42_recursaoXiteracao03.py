import time

"Para expliar melhor a principal diferença entre recursão e iteração, podemos citar o tempo na chamada de funções"
"Na recursão, cada vez que uma função é chamada, uma nova pilha de execução é criada para armazenar as variáveis locais e o estado da função. Isso pode levar a um aumento significativo no tempo de execução, especialmente para problemas que exigem muitas chamadas recursivas. Por outro lado, na iteração, o código é executado em um loop, e não há necessidade de criar novas pilhas de execução para cada iteração. Isso pode resultar em um tempo de execução mais rápido para problemas que podem ser resolvidos usando iteração."
"Além disso, a recursão pode levar a um consumo excessivo de memória, especialmente para problemas que exigem muitas chamadas recursivas. Isso ocorre porque cada chamada recursiva cria uma nova pilha de execução, e se o número de chamadas recursivas for muito grande, isso pode levar a um estouro de pilha. Por outro lado, a iteração geralmente consome menos memória, pois não há necessidade de criar novas pilhas de execução para cada iteração."
"Em resumo, a recursão pode ser mais elegante e fácil de entender para problemas que têm uma estrutura recursiva natural, mas pode levar a um aumento significativo no tempo de execução e consumo de memória. A iteração pode ser mais eficiente em termos de tempo de execução e uso de memória para problemas que não têm uma estrutura recursiva clara, mas pode ser menos elegante e mais difícil de entender para problemas que têm uma estrutura recursiva natural."
"Para exemplificar, vamos comparar o tempo de execução de um número usando recursão e iteração. Para isso, podemos usar a biblioteca time para medir o tempo de execução e a biblioteca memory_profiler para medir o consumo de memória. "
"Vamo usar a sequência de Fibonacci como exemplo, pois ela é um exemplo clássico de um problema que pode ser resolvido usando recursão e iteração. A sequência de Fibonacci é uma sequência de números em que cada número é a soma dos dois números anteriores, começando com 0 e 1. Por exemplo, os primeiros 10 números da sequência de Fibonacci são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34."
"Vamos calcular o n-ésimo número da sequência de Fibonacci usando recursão e iteração, e medir o tempo de execução e consumo de memória para cada abordagem. Para isso, podemos usar o seguinte código:"


def fib_recursivo(n):
    if n <= 1:
        return n
    return fib_recursivo(n - 1) + fib_recursivo(n - 2)


print(fib_recursivo(30))


def medir_fib_recursivo(n):
    start_time = time.time()
    result = fib_recursivo(n)
    end_time = time.time()
    print(
        f"Fibonacci recursivo({n}) = {result}, tempo de execução: {end_time - start_time} segundos"
    )


medir_fib_recursivo(30)
