for x in range(0, 11):
    print(x)
    "Chat me ajuda fazer uma função que retorne a contagem dos numeros printados do for in range"

    def count_numbers(start, end):
        return end - start

    result = count_numbers(0, 11)
print(f"Total de números: {result}")

# A contagem aparece para cada iteração do loop porque o print(f"Total de números: {result}")
# está DENTRO do for loop. Isso faz com que a mensagem seja exibida 11 vezes (uma por iteração).
# Para exibir apenas uma vez, mova o print() PARA FORA do for loop (desindente).
"Olha como a hidentação é importante"
