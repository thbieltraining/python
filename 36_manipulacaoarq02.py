with open("C:\\ARQ\\Ola meu nome é Nathan GABRIEL.txt", "r") as infile:

    content = infile.read()
    print(content)

with open("C:\\ARQ\\Ola meu nome é Nathan GABRIEL.txt", "a") as outfile:
    outfile.write(", tenho 21 anos e moro no Brasil")
