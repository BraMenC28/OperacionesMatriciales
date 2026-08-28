import random
class Ordenamiento:
    def __init__(self,numeros):
        self.numeros=numeros#numero es igual al tamaño del vector 
        self.resultado=[]
    def getResultado(self):#el get busca un valor y si no existe no genera error si no devuelve none 
        return self.resultado
    def burbuja(self):
        vector=[]
        for i in range(self.numeros):
            numRandom = float(random.uniform(1, 100))
            vector.append(numRandom)
        print("Lista original:")
        print(vector)
        for i in range(len(vector) - 1):#len(lista) dara al for la cantidad de veces que el porgrama repite la accion y le resta uno por pasada 
            for j in range(len(vector) - 1 - i):#cuando el numero mayor queda al final hace que el programa ya no recorra esa posicion 

                if vector[j] > vector[j + 1]:
                 vector[j], vector[j + 1] = vector[j + 1], vector[j]
        self.resultado = vector
    def inserccion(self):
        vector=[]
        for i in range(self.numeros):
            numRandom = float(random.uniform(1, 100))
            vector.append(numRandom)
        print("Lista original:")
        print(vector)
        for i in range(1, len(vector)):
            actual = vector[i]
            j = i - 1
            while j >= 0 and vector[j] > actual:
                vector[j + 1] = vector[j]
                j = j - 1
            vector[j + 1] = actual
        self.resultado = vector
    def seleccion(self):
        vector=[]
        for i in range(self.numeros):
            numRandom = float(random.uniform(1, 100))
            vector.append(numRandom)
        print("Lista original:")
        print(vector)
        for i in range(len(vector) - 1):
            menor = i
            for j in range(i + 1, len(vector)):
                if vector[j] < vector[menor]:
                    menor = j
            vector[i], vector[menor] = vector[menor], vector[i]
        self.resultado = vector
    def merge(self, vector=None):
        if vector is None:
            vector = []
            for i in range(self.numeros):
                numRandom = float(random.uniform(1, 100))
                vector.append(numRandom)
            print("Lista original:")
            print(vector)
        if len(vector) <= 1:
            self.resultado = vector
            return vector
        mitad = len(vector) // 2
        izquierda = vector[:mitad]
        derecha = vector[mitad:]
        izquierda = self.merge(izquierda)
        derecha = self.merge(derecha)
        resultado = []
        i = 0
        j = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        self.resultado = resultado
        return resultado