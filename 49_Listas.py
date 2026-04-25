"Listas e suas variações, boraaa"

" Listas são estruturas de dados que armazenam uma coleção de itens. Elas são mutáveis, o que significa que você pode alterar seus elementos após a criação. As listas em Python são definidas usando colchetes [] e os elementos são separados por vírgulas."

"Os tipos de listas incluem: Listas Simples, Listas Duplamente Ligadas, Listas Circulares, Listas de Comprimento Variável, Listas de Comprimento Fixo, Listas Aninhadas, Listas de Objetos, Listas de Funções, Listas de Dicionários, Listas de Conjuntos e Listas de Tuplas."
"Listas também possuem métodos de aplicações : Sequencial, Encadeada, Estatica, Dinâmica, Circular, Duplamente Encadeada, Aninhada, Heterogênea, Homogênea, Ordenada, Desordenada, Mutável e Imutável."
"Mas hoje vamos falar mais sobre Sequencial, Encadeada, Estática e Dinâmica."

"Sequencial: Os elementos são armazenados em posições contíguas na memória. Acesso rápido, mas inserção e remoção podem ser lentas devido à necessidade de deslocar elementos.Podem ser acessados por indice, o que torna o acesso rápido. No entanto, a inserção e remoção de elementos podem ser lentas, pois pode ser necessário deslocar outros elementos para manter a ordem."
"Encadeada: Cada elemento (nó) contém um valor e uma referência para o próximo nó. Permite inserção e remoção eficientes, mas o acesso é mais lento devido à necessidade de percorrer a lista."

"Quando usar Sequencial: Quando você precisa de acesso rápido a elementos por índice e não se importa com a eficiência de inserção e remoção. Exemplo: Listas de tarefas, onde a ordem é importante e o acesso rápido é necessário."
"Quando usar Encadeada: Quando você precisa de inserção e remoção eficientes, especialmente em listas grandes, e o acesso por índice não é uma prioridade. Exemplo: Implementação de filas ou pilhas, onde a ordem de inserção e remoção é importante."

"Estática: O tamanho da lista é fixo e definido no momento da criação. Não pode ser redimensionada, o que pode levar a desperdício de memória se o tamanho for superestimado ou falta de espaço se for subestimado."
"Dinâmica: O tamanho da lista pode ser alterado durante a execução do programa. Permite adicionar ou remover elementos conforme necessário, mas pode ter overhead de memória devido à necessidade de redimensionamento."

"Quando usar Estática: Quando você conhece o número exato de elementos que a lista conterá e deseja evitar o overhead de redimensionamento. Exemplo: Armazenar os dias da semana, onde o número de elementos é fixo."
"Quando usar Dinâmica: Quando o número de elementos na lista pode variar durante a execução do programa e você deseja flexibilidade. Exemplo: Armazenar uma lista de usuários em um sistema, onde o número de usuários pode aumentar ou diminuir ao longo do tempo."

"Outras variações incluem : "

"Ordenada: Os elementos são mantidos em uma ordem específica, como crescente ou decrescente. Isso pode facilitar a busca e a organização dos dados, mas pode exigir mais tempo para inserção e remoção de elementos."
"Desordenada ou Não Ordenada: Os elementos não seguem uma ordem específica. Isso pode permitir inserção e remoção mais rápidas, mas pode dificultar a busca e a organização dos dados."

"Linear: Os elementos são organizados em uma sequência linear, onde cada elemento tem um predecessor e um sucessor (exceto o primeiro e o último). Isso é comum em listas encadeadas e arrays."
"Não Linear: Os elementos não seguem uma sequência linear, podendo ter múltiplos predecessores e sucessores. Isso é comum em estruturas como árvores e grafos."

"Homogênea: Todos os elementos da lista são do mesmo tipo. Isso pode facilitar a manipulação dos dados, mas pode limitar a flexibilidade. Exemplo: Uma lista de números inteiros."
"Heterogênea: Os elementos da lista podem ser de tipos diferentes. Isso pode aumentar a flexibilidade, mas pode exigir mais cuidado na manipulação dos dados. Exemplo: Uma lista que contém números, strings e objetos."

"Mutável: Os elementos da lista podem ser alterados após a criação da lista. Isso é comum em listas em Python, onde você pode adicionar, remover ou modificar elementos. Exemplo: Uma lista de tarefas que pode ser atualizada conforme necessário."
"Imutável: Os elementos da lista não podem ser alterados após a criação da lista. Isso é comum em tuplas em Python, onde os elementos são fixos e não podem ser modificados. Exemplo: Uma tupla que contém as coordenadas de um ponto no espaço (x, y)."

"Vamos ver um exemplo de implementação de uma lista encadeada em Python:"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


# Exemplo de uso
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.print_list()
"Neste exemplo, criamos uma classe Node para representar cada nó da lista encadeada, que contém um valor (data) e uma referência para o próximo nó (next). A classe LinkedList gerencia a lista, permitindo adicionar novos nós e imprimir os valores da lista. A função append adiciona um novo nó ao final da lista, enquanto a função print_list percorre a lista e imprime os valores de cada nó."
