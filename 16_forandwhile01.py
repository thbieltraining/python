S = "NUMEROS"
for c in S:
    if c in "aeiouAEIOU":
        print(c)
"Qual função que contaria o numero de vogais e retornaria ele para mim ?"
print(sum(1 for c in S if c in "aeiouAEIOU"))
