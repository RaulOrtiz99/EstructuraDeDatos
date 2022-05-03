from mimetypes import init


class Arbol:
    
    def __init__(self,valor):
        self.raiz= None 
        pass

    #METODOS DE LOS ARBOLES BINARIOS

    #INSERTAR -> insertar un valor en el arbol binario
    #ES VACIO -> Devuelte TRUE si esta vacio
    #Es HOJA -> Devuelve TRUE si el arbol no tiene ni hijo izquierdo ni hijo derecho eso quiere decir que es hoja
    #BUSCAR -> Busca un nodo por su valor
    #RECORRIDO POST ORDEN
    #RECORRIDO PRE ORDEN
    #RECORRIDO INORDEN
    #METODO ES RAMA -> Devuelve verdadero si es una rama