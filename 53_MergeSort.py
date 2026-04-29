"Merge Sort agora, seguindo a estrutura da aula de hoj do professor."

"Lembrando que o Merge Sort é um algoritmo de ordenação do tipo 'dividir para conquistar', onde o array é dividido em subarrays menores, ordenados recursivamente e depois mesclados para formar um array ordenado."
"O código a seguir implementa o Merge Sort em Python, seguindo a estrutura típica de uma função recursiva para dividir o array e uma função auxiliar para mesclar os subarrays ordenados."


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir o array em duas metades
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Mesclar as duas metades ordenadas
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Mesclar os elementos dos dois subarrays
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Adicionar os elementos restantes do subarray esquerdo, se houver
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Adicionar os elementos restantes do subarray direito, se houver
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


"Esse código ficou maior, mas é melhor estruturado e mais fácil de entender, seguindo a lógica do algoritmo de divisão e conquista. A função 'merge_sort' é responsável por dividir o array e chamar a função 'merge' para mesclar os subarrays ordenados."

# Exemplo de uso
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# Saída: [3, 9, 10, 27, 38,43, 82]
"Como podemos ver, o Merge Sort é eficiente para ordenar grandes conjuntos de dados, com uma complexidade de O(n log n) em todos os casos, o que o torna uma escolha popular para muitos tipos de aplicações de ordenação."
