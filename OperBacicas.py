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
            self.resultado=print(*i)
        return self.resultado