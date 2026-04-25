"Agora é a hora de falarmos sobre árvores em Python"

"Uma árvore é uma estrutura de dados hierárquica que consiste em nós conectados por arestas. Cada nó pode ter zero ou mais filhos, e um nó sem filhos é chamado de folha. A árvore tem um nó raiz, que é o ponto de partida da estrutura."
"Arvores são listas não lineares, onde cada elemento pode ter múltiplos filhos, ao contrário de listas lineares onde cada elemento tem no máximo um sucessor. Elas são usadas para representar hierarquias, como a estrutura de diretórios em um sistema de arquivos ou a organização de uma empresa."

"Existem vários tipos de árvores, incluindo:"

" - Árvore Binária: Cada nó tem no máximo dois filhos."
" - Árvore N-ária: Cada nó pode ter no máximo N filhos."
" - Árvore de Busca Binária: Uma árvore binária onde os nós são organizados de forma que o valor do nó esquerdo é menor que o valor do nó pai, e o valor do nó direito é maior que o valor do nó pai."
" - Árvore AVL: Uma árvore de busca binária auto-balanceada, onde a diferença de altura entre as subárvores esquerda e direita de qualquer nó é no máximo 1."

"Algumas terminologias importantes relacionadas a árvores incluem:"

"Raiz: O nó principal da árvore, que não tem pai."
"Filho: Um nó que é diretamente conectado a outro nó acima dele (o pai)."
"Pai: Um nó que tem um ou mais filhos."
"Irmãos: Nós que compartilham o mesmo pai."
"Subárvore: Uma parte da árvore que consiste em um nó e todos os seus descendentes."
"Altura: O número de arestas no caminho mais longo da raiz até uma folha."
"Profundidade: O número de arestas do nó até a raiz."
"Árvores são usadas em muitas aplicações, como sistemas de arquivos, bancos de dados, algoritmos de busca e muito mais. Elas permitem organizar dados de forma hierárquica e eficiente para operações como inserção, remoção e busca."

"Vamos ver um exemplo de implementação de uma árvore binária em Python, onde cada nó tem no máximo dois filhos (esquerdo e direito):"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def inorder_traversal(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        res = []
        if node:
            res = self._inorder_recursive(node.left)
            res.append(node.data)
            res = res + self._inorder_recursive(node.right)
        return res


# Exemplo de uso
binary_tree = BinaryTree()
binary_tree.insert(10)
binary_tree.insert(5)
binary_tree.insert(15)
binary_tree.insert(3)
binary_tree.insert(7)
print("Inorder Traversal:", binary_tree.inorder_traversal())
# A travessia em ordem (inorder) de uma árvore binária de busca retorna os elementos em ordem crescente. Neste exemplo, a saída será: [3, 5, 7, 10, 15], pois os elementos são inseridos de forma que o valor do nó esquerdo é menor que o valor do nó pai, e o valor do nó direito é maior que o valor do nó pai.
