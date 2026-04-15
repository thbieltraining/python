import random


class MyList(list):
    def choice(self):
        return random.choice(self)


L = MyList([1, 2, 3, 4, 5])
print(L.choice())

"Tem que ter atenção ao usar herança, pois se a classe filha não tiver o método que a classe pai tem, ela não vai funcionar"
