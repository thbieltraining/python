a = [3, 4, 5]
b = a
b[1] = 10
print(a)
print(b)
"A e B apontam para a mesma lista, então quando alteramos o valor do índice 1 de B, isso também altera o valor do índice 1 de A, pois ambos estão referenciando a mesma lista na memória"
