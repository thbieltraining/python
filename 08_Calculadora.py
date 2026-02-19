import os
import sys

# Operações aritméticas com entrada e saída imediata
"""
Uso:
- Salve o arquivo e execute com Python 3 no terminal:
    python "C:/caminho/para/o/arquivo.py"
    ou (Windows)
    py "C:/caminho/para/o/arquivo.py"

O que o programa faz:
- Pede dois números (use ponto para decimais).
- Exibe: adição, subtração, multiplicação, divisão, potência e resto.

Dicas:
- Evite digitar 0 como segundo número (divisão/reste por zero causa ZeroDivisionError).
- No VS Code: abra o arquivo e selecione "Run Python File in Terminal" ou pressione F5.
- Para automatizar, rode em um ambiente com Python 3.x instalado.
"""

print("=== Calculadora Simples ===\n")

# Entrada
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Operações e saída imediata
print(f"Adição: {num1} + {num2} = {num1 + num2}")
print(f"Subtração: {num1} - {num2} = {num1 - num2}")
print(f"Multiplicação: {num1} * {num2} = {num1 * num2}")
print(f"Divisão: {num1} / {num2} = {num1 / num2}")
print(f"Potência: {num1} ** {num2} = {num1 ** num2}")
print(f"Resto: {num1} % {num2} = {num1 % num2}")

while True:
    resp = input("\nDeseja fazer outro cálculo? [S/n]: ").strip().lower()
    if resp in ("", "s", "sim", "si"):
        os.system("cls" if os.name == "nt" else "clear")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    if resp in ("n", "nao", "não", "no"):
        print("Encerrando...")
        break
    print("Resposta inválida. Digite S para sim ou N para não.")
    # Eu gostei muuito desse programa, eu usei o Claude para desbravar algumas funcionalidades que eu não conhecia... muuito massaaaa!!!
