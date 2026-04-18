import time

"Como vimos, iteração e recursão são duas abordagens para resolver problemas que envolvem repetição. A iteração utiliza estruturas de controle de fluxo, como loops, para repetir um bloco de código até que uma condição seja satisfeita. Já a recursão é uma técnica onde uma função chama a si mesma para resolver um problema, dividindo-o em subproblemas menores."
"Tambem vimos que a recursão pode ser elegante e fácil de entender, mas pode levar a problemas de desempenho e estouro de pilha e tempo de execução se não for usada com cuidado e devida análise. A iteração, por outro lado, é geralmente mais eficiente em termos de tempo e memória, mas pode ser menos intuitiva para problemas que naturalmente se encaixam em uma estrutura recursiva."
"Mas ainda não está perdido para recursão, vamos agora falar de memorização, que é uma técnica de otimização que armazena os resultados de chamadas de função para evitar cálculos redundantes. Isso pode melhorar significativamente o desempenho de funções recursivas, especialmente aquelas que têm muitos subproblemas sobrepostos, como a sequência de Fibonacci."
"Vamos agora usar recursão com memorização para calcular o n-ésimo número da sequência de Fibonacci, e medir o tempo de execução para essa abordagem. Para isso, podemos usar o seguinte código:"


m = {}


def fib(n):
    if n < 2:
        return 1
    if n in m:
        return m[n]
    elif m.get(n) is not None:
        return m[n]
    else:
        m[n] = fib(n - 1) + fib(n - 2)
        return m[n]


def medir_fib(n):
    start_time = time.time()
    result = fib(n)
    end_time = time.time()
    print(
        f"Fibonacci({n}) = {result}, tempo de execução: {end_time - start_time} segundos"
    )


medir_fib(30)
