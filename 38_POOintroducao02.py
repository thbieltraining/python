class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)


p = input("Digite as coordenadas do ponto (x, y): ")
x, y = map(float, p.split(","))
point = Point(x, y)
print(point)

"Que codigo complicado, no decorrer das semanas vamos aprender a fazer isso de uma maneira mais simples, usando o método __init__ para criar o objeto e atribuir os valores de x e y diretamente, sem precisar de métodos set_x e set_y. Além disso, vamos aprender a usar o método __repr__ para representar o objeto de forma mais legível. E também vamos aprender a usar o método __add__ para somar dois pontos ou um ponto com um número, tornando nosso código mais flexível e fácil de usar."
"Será que herança pode nos judar a simplificar ainda mais esse código? Vamos descobrir nas próximas aulas!"
"Aprender usando IA tornou muuito mais fácil, mas confesso que interagir xom ela e não com pessoas é meio doido ainda kkkk"
