"Primeiro vamos falar sobre o que é uma recursão e o que é uma iteração. A recursão é um processo em que uma função chama a si mesma para resolver um problema. Já a iteração é um processo em que um bloco de código é repetido várias vezes até que uma condição seja satisfeita."

"Aco que a melhor forma da gente entender a diferença entre recursão e iteração é através de um exemplo. Vamos supor que queremos calcular o fatorial de um número. O fatorial de um número n é o produto de todos os números inteiros positivos menores ou iguais a n. Por exemplo, o fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120. "
"Podemos calcular o fatorial de um número usando recursão da seguinte forma:"


def fat(n):
    if n == 0:
        return 1
    else:
        RESULTADO = n * fat(n - 1)
        return RESULTADO


print(fat(5))
