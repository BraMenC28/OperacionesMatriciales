class OpBasicas:
    def __init__(self, matriz_1, matriz_2, resultado):
        self.matriz_1=matriz_1
        self.matriz_2=matriz_2
        self.resultado=resultado
    def sumaMatriz(self, filas, columnas):  
        self.resultado=[]
        for i in range (filas):
            fila=[]
            for j in range (columnas):
                fila.append(self.matriz_1[i][j]+self.matriz_2[i][j])
            self.resultado.append(fila)
    def getResultado(self):
        for i in self.resultado:
            print(*i)
        return self.resultado
    def Multiplicar(self, fil_1, colum_1, fil_2, colum_2):
        self.resultado = [[0 for _ in range(colum_2)] for _ in range(fil_1)]#Se crea la matriz para que luego se cambien los valores
        for i in range(fil_1):
            for j in range(colum_2):
                for k in range(colum_1):
                    self.resultado[i][j]+=(self.matriz_1[i][k]*self.matriz_2[k][j])#proceso para la multiplicacion de matrices
    