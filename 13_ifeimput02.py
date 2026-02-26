a = input("Digite algo: ")
print(f"Você digitou: {a}")
"To querendo agora usar um if para tranformar o digito em um float ou em str, dependendo de como o usuario digitar "
# Você pode usar um bloco try-except para tentar converter o input para float e, se falhar, manter como string. Aqui está um exemplo:"
try:
    a = float(a)
    if a.is_integer():
        a = int(a)  # Converte para inteiro se for um número inteiro
except ValueError:
    pass  # Mantém a como string se não for possível converter para float
print(f"Você digitou: {a} (tipo: {type(a)})")
