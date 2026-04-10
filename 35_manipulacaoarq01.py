import os

infile = open("C:\\ARQ\\Ola meu nome é Nathan GABRIEL.txt", "r")
content = infile.read()
print(content)
infile.close()

"Como faço para o arquivo python reconhecer os caracteres especiais?"
infile = open("C:\\ARQ\\Ola meu nome é Nathan GABRIEL.txt", "r", encoding="utf-8")
"Eu escrevi isso porquê meu arquivo de texto tem acentos, e sem o encoding ele não reconhece os caracteres acentuados, e aparece um monte de símbolos no lugar dos acentos"

file_size = os.path.getsize("C:\\ARQ\\Ola meu nome é Nathan GABRIEL.txt")
print(f"Tamanho do arquivo: {file_size} bytes")

"""
Módulo para ler arquivos com encoding de caracteres especiais e recuperar informações de tamanho.
Este módulo demonstra:
1. Leitura de arquivos de texto com encoding UTF-8 para manipular caracteres acentuados corretamente
2. Cálculo do tamanho do arquivo usando os.getsize()
3. Compreensão da diferença entre tamanho exibido e tamanho real em bytes

Conceito-chave: Discrepância entre tamanho no gerenciador de arquivos (31 KB) e resultado de os.getsize()
- Gerenciadores de arquivos frequentemente exibem tamanho em unidades binárias (1 KB = 1024 bytes)
- os.getsize() retorna o tamanho exato do arquivo em bytes
- 31 KB (exibido) ≈ 31 . 1024 = 31.744 bytes (real)
- A diferença existe porque gerenciadores usam binário (KiB) enquanto às vezes informam como KB
- Além disso, sistemas de arquivos alocam storage em clusters, então o espaço em disco realmente usado 
    pode ser maior que o tamanho lógico do arquivo

Nota sobre Encoding UTF-8:
- Caracteres acentuados (como 'é', 'ã') requerem especificação de encoding
- Sem encoding="utf-8", Python pode usar o encoding padrão do sistema
- Isso causa caracteres especiais exibirem como símbolos garrados ou desconhecidos
# Converter bytes para KB (usando 1 KB = 1024 bytes)
file_size_kb = file_size / 1024
print(f"Tamanho do arquivo: {file_size_kb:.2f} KB")

# Ou usar a biblioteca humana para formatação automática
file_path = Path("C:\\ARQ\\Ola meu nome é Nathan GABRIEL.txt")
print(f"Tamanho: {file_path.stat().st_size / 1024:.2f} KB")

"""
