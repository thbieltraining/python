"Vamos agora usar iteração para calcular o n-ésimo número da sequência de Fibonacci, e medir o tempo de execução para essa abordagem. Para isso, podemos usar o seguinte código:"

import time


def fib_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def medir_fib_iterativo(n):
    start_time = time.time()
    result = fib_iterativo(n)
    end_time = time.time()
    print(result)
    print(
        f"Fibonacci iterativo({n}) = {result}, tempo de execução: {end_time - start_time} segundos"
    )


medir_fib_iterativo(30)
