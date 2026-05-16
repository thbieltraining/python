from tkinter import Tk, Label, PhotoImage, TOP

"Vamos manipular algumas imagens usando photoimage, uma biblioteca de processamento de imagens em Python. Primeiro, vamos importar a biblioteca e carregar uma imagem para manipular."

root = Tk()

photo = PhotoImage(file="naruto_gif.gif").subsample(1)

image = Label(master=root, image=photo)
image.pack(side=TOP)

text = Label(master=root, text="naruto_gif.gif")
text.pack()

root.mainloop()
"Neste código, criamos uma janela usando Tkinter e carregamos uma imagem chamada 'naruto_gif.gif' usando a classe PhotoImage. Em seguida, exibimos a imagem em um rótulo (Label) e adicionamos um texto abaixo dela. Por fim, iniciamos o loop principal da interface gráfica para exibir a janela."
