from collections import deque

class No:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.altura = 1

class AVL:
    def __init__(self):
        self.root = None
        self._tamanho = 0  

    def get_altura(self, node):
        return node.altura if node else 0
    
    def get_balanco(self, node):
        return self.get_altura(node.left) - self.get_altura(node.right) if node else 0
    
    def girar_direita(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.altura = 1 + max(self.get_altura(z.left), self.get_altura(z.right))
        y.altura = 1 + max(self.get_altura(y.left), self.get_altura(y.right))

        return y
    
    def girar_esquerda(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.altura = 1 + max(self.get_altura(z.left), self.get_altura(z.right))
        y.altura = 1 + max(self.get_altura(y.left), self.get_altura(y.right))

        return y
    
    def insere(self, key):
        self.root = self._insere(self.root, key)
        self._tamanho += 1  

    def _insere(self, node, key):
        if not node:
            return No(key)
        
        if key < node.key:
            node.left = self._insere(node.left, key)
        elif key > node.key:
            node.right = self._insere(node.right, key)
        else:
            return node  
        
        node.altura = 1 + max(self.get_altura(node.left), self.get_altura(node.right))

        balanco = self.get_balanco(node)

        if balanco > 1 and key < node.left.key:
            return self.girar_direita(node)

        if balanco < -1 and key > node.right.key:
            return self.girar_esquerda(node)

        if balanco > 1 and key > node.left.key:
            node.left = self.girar_esquerda(node.left)
            return self.girar_direita(node)

        if balanco < -1 and key < node.right.key:
            node.right = self.girar_direita(node.right)
            return self.girar_esquerda(node)

        return node
    
    def contem(self, key):
        return self._contem(self.root, key)
    
    def _contem(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._contem(node.left, key)
        else:
            return self._contem(node.right, key)
    
    def remove(self, key):
        self.root = self._remove(self.root, key)
        self._tamanho -= 1  

    def _remove(self, node, key):
        if not node:
            return node
        
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.right = self._remove(node.right, temp.key)
        
        if not node:
            return node
        
        node.altura = 1 + max(self.get_altura(node.left), self.get_altura(node.right))

        balanco = self.get_balanco(node)

        if balanco > 1 and self.get_balanco(node.left) >= 0:
            return self.girar_direita(node)

        if balanco < -1 and self.get_balanco(node.right) <= 0:
            return self.girar_esquerda(node)

        if balanco > 1 and self.get_balanco(node.left) < 0:
            node.left = self.girar_esquerda(node.left)
            return self.girar_direita(node)

        if balanco < -1 and self.get_balanco(node.right) > 0:
            node.right = self.girar_direita(node.right)
            return self.girar_esquerda(node)

        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def geraLista(self):
        lista = []
        self._em_ordem(self.root, lista)
        return lista
    
    def _em_ordem(self, node, lista):
        if node:
            self._em_ordem(node.left, lista)
            lista.append(node.key)
            self._em_ordem(node.right, lista)
    
    def altura(self):
        return self.get_altura(self.root)
    
    def tamanho(self):
        return self._tamanho

avl = AVL()
avl.insere(10)
avl.insere(20)
avl.insere(30)
avl.insere(40)
avl.insere(50)
avl.insere(25)

print("Contem 25?", avl.contem(25))  
print("Contem 100?", avl.contem(100))  

print("Lista de elementos:", avl.geraLista()) 
print("Altura da arvore:", avl.altura())  
print("Tamanho da arvore:", avl.tamanho()) 

avl.remove(25)
print("Lista apos remover 25:", avl.geraLista()) 
print("Tamanho apos remover:", avl.tamanho())  