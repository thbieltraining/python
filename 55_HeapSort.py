"Agora um que não falamos, Heap Sort."

"Heap Sort é um algoritmo de ordenação baseado em uma estrutura de dados chamada heap, que é uma árvore binária completa onde cada nó é maior (ou menor) do que seus filhos. O Heap Sort funciona construindo um heap a partir dos elementos do array e, em seguida, repetidamente removendo o elemento máximo (ou mínimo) do heap e reconstruindo o heap até que ele esteja vazio. O resultado é um array ordenado. O Heap Sort tem uma complexidade de O(n log n) em todos os casos, o que o torna eficiente para grandes conjuntos de dados."
"Vimo uma introdução dele no arquivo 50, mas agora vamos implementar o Heap Sort em Python para entender melhor como ele funciona na prática do código subscrito."


def heapify(arr, n, i):
    largest = i  # Inicializa o maior como raiz
    L = 2 * i + 1  # Esquerda = 2*i + 1
    r = 2 * i + 2  # Direita = 2*i + 2

    # Verifica se o filho esquerdo existe e é maior que a raiz
    if L < n and arr[L] > arr[largest]:
        largest = L

    # Verifica se o filho direito existe e é maior que o maior até agora
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Se o maior não for a raiz, troca e continua heapificando
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca

        # Recursivamente heapifica a subárvore afetada
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Constrói um heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Um por um extrai os elementos do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Troca
        heapify(arr, i, 0)

    return arr


print(heap_sort([12, 11, 13, 5, 6, 7]))
# Saída: [5, 6, 7, 11, 12, 13]
"Esse código implementa o Heap Sort em Python. A função 'heapify' é responsável por manter a propriedade do heap, enquanto a função 'heap_sort' constrói o heap e extrai os elementos para ordenar o array. O resultado é um array ordenado em ordem crescente."
