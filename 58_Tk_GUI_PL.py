from PIL import Image

"Vamo agora brincar com uma imagem usando pillow, mas antes, o  que é pillow? "
"Pillow é uma biblioteca de processamento de imagens em Python. Ela é uma ramificação da biblioteca PIL (Python Imaging Library) e oferece uma ampla gama de funcionalidades para abrir, manipular e salvar imagens em vários formatos. Com Pillow, você pode realizar operações como redimensionamento, rotação, corte, aplicação de filtros, adição de texto e muito mais. É uma ferramenta poderosa para trabalhar com imagens em projetos de desenvolvimento, automação e análise de dados."
"Vamos começar instalando a biblioteca Pillow. Você pode fazer isso usando pip, o gerenciador de pacotes do Python. Abra o terminal e execute o seguinte comando:"

"Depois de instalar a biblioteca, você pode começar a usá-la em seu código Python. Aqui está um exemplo simples de como abrir uma imagem, redimensioná-la e salvá-la com um novo nome:"

# Abrindo a imagem
imagem = Image.open("C:\\Users\\Pichau\\.vscode\\python\\IMG\\mitogui.jpg")
# Criando uma copia da imagem
imagem_copia = imagem.copy()
# Redimensionando a imagem
imagem_redimensionada = imagem.copy()
imagem_redimensionada = imagem_redimensionada.resize((200, 200))
# Salvando a imagem redimensionada
imagem_redimensionada.save(
    "C:\\Users\\Pichau\\.vscode\\python\\IMG\\mitogui_redimensionada.jpg"
)
