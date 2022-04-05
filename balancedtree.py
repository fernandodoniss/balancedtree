class BinaryTree:
    def __init__(self,dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

def insertar(root,nuevoV):
    if root is None:
        root = BinaryTree(nuevoV)
        return root
    
    if nuevoV<root.dato:
        root.izquierda=insertar(root.izquierda,nuevoV)
    else:
        root.derecha=insertar(root.derecha,nuevoV)
    return root

def altura(root):

    if root==None:
        return 0
    alturaIzquierda=altura(root.izquierda)
    alturaDerecha=altura(root.derecha)

    if alturaIzquierda>alturaDerecha:
        return alturaIzquierda +1
    else:
        return alturaDerecha +1

def balanced(root):
    if root==None:
        return True
    lAltura = altura(root.izquierda)
    rAltura = altura(root.derecha)
    if(abs(lAltura-rAltura)>1):
        return False
    lVeri=balanced(root.izquierda)
    rVeri=balanced(root.derecha)

    if lVeri==True and rVeri==True:
        return True

root=insertar(None,15)
insertar(root,10)
insertar(root,25)
insertar(root,6)
insertar(root,14)
insertar(root,20)
insertar(root,60)
print("Printing True if binary tree is balanced:")
print(balanced(root))