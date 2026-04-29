"Vamos agora começar a falar de Algoritmos clássicos de ordenação"

"Algoritmos de ordenação são fundamentais em ciência da computação e são usados para organizar dados de maneira eficiente. Existem vários algoritmos de ordenação, cada um com suas próprias características, vantagens e desvantagens. Alguns dos algoritmos de ordenação mais comuns incluem: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort e Quick Sort."
"Vamos dar uma breve descrição de cada um desses algoritmos:"

"1. Bubble Sort: É um algoritmo simples que compara elementos adjacentes e os troca se estiverem na ordem errada. Ele é fácil de entender, mas não é eficiente para grandes conjuntos de dados, com uma complexidade de O(n^2)."

"2. Selection Sort: Este algoritmo divide a lista em duas partes: a parte ordenada e a parte não ordenada. Ele seleciona o menor elemento da parte não ordenada e o troca com o primeiro elemento da parte não ordenada. A complexidade também é O(n^2)."

"3. Insertion Sort: Este algoritmo constrói a lista ordenada um item de cada vez, pegando cada elemento da lista e inserindo-o na posição correta na parte ordenada. Ele é eficiente para listas pequenas ou quase ordenadas, com uma complexidade de O(n^2) no pior caso."

"4. Merge Sort: Este é um algoritmo de ordenação eficiente que utiliza a técnica de divisão e conquista. Ele divide a lista em duas metades, ordena cada metade recursivamente e depois as mescla para obter a lista ordenada final. A complexidade é O(n log n) em todos os casos."

"5. Quick Sort: Este é outro algoritmo de ordenação eficiente que também utiliza a técnica  de divisão e conquista. Ele seleciona um elemento como pivô e particiona a lista em duas partes: os elementos menores que o pivô e os elementos maiores que o pivô. Em seguida, ele ordena recursivamente as duas partes. A complexidade média é O(n log n), mas no pior caso pode ser O(n^2) se o pivô for escolhido de maneira inadequada."

"Cada um desses algoritmos tem suas próprias vantagens e desvantagens, e a escolha do algoritmo de ordenação adequado depende do tamanho dos dados, da natureza dos dados e dos requisitos de desempenho."
"Vamos agora implementar cada um desses algoritmos de ordenação em Python para entender melhor como eles funcionam na prática."


# Implementação do Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Implementação do Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Implementação do Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Implementação do Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# Implementação do Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x < pivot]
        greater_than_pivot = [x for x in arr[1:] if x >= pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


# Exemplo de uso dos algoritmos de ordenação
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", arr)
    print("Bubble Sort:", bubble_sort(arr.copy()))
    print("Selection Sort:", selection_sort(arr.copy()))
    print("Insertion Sort:", insertion_sort(arr.copy()))
    print("Merge Sort:", merge_sort(arr.copy()))
    print("Quick Sort:", quick_sort(arr.copy()))
