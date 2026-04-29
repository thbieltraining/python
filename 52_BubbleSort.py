"Bora começar do começo : Bubble Sort"

"Lógica: comparar o elemento atual com o próximo, se o próximo for menor, trocar os dois. Repetir isso até o final da lista, e depois repetir todo o processo até que a lista esteja ordenada."


def bubble_sort(v):
    for i in range(len(v) - 1):
        for j in range(len(v) - i - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
    return v


print(bubble_sort([5, 1, 4, 2, 8]))
# Saída: [1, 2, 4, 5, 8]
"Aqui támbem vemos um código mais limpo, sem a necessidade de criar uma variável auxiliar para a troca dos elementos e fazendo a mesma coisa do código do arquivo anteior, mas de uma forma mais simples e direta."
