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
    def Inversa(self, filas, columnas):
        self.resultado = []
        # Validación de matriz cuadrada (requisito matemático)
        if filas != columnas:
            print("Error: La matriz debe ser cuadrada (mismas filas y columnas) para tener inversa.")
            return
        # 1. Crear una copia de matriz_1 para no modificar los valores originales
        matriz_copia = []
        for i in range(filas):
            fila_nueva = []
            for j in range(columnas):
                fila_nueva.append(float(self.matriz_1[i][j]))
            matriz_copia.append(fila_nueva)
        # 2. Crear la matriz identidad del mismo tamaño
        matriz_identidad = []
        for i in range(filas):
            fila_identidad = []
            for j in range(columnas):
                if i == j:
                    fila_identidad.append(1.0)
                else:
                    fila_identidad.append(0.0)
            matriz_identidad.append(fila_identidad)
        # 3. Aplicar el método de Gauss-Jordan
        for i in range(filas):
            # Pivoteo: Si el elemento en la diagonal principal es 0, buscamos una fila debajo para intercambiar
            if matriz_copia[i][i] == 0.0:
                for k in range(i + 1, filas):
                    if matriz_copia[k][i] != 0.0:
                        # Intercambiar las filas completas
                        matriz_copia[i], matriz_copia[k] = matriz_copia[k], matriz_copia[i]
                        matriz_identidad[i], matriz_identidad[k] = matriz_identidad[k], matriz_identidad[i]
                        break
                else:
                    print("Error: La matriz es singular (su determinante es 0) y no tiene inversa.")
                    return
            # Dividir toda la fila actual por el valor del pivote para que la diagonal sea 1
            pivote = matriz_copia[i][i]
            for j in range(columnas):
                matriz_copia[i][j] = matriz_copia[i][j] / pivote
                matriz_identidad[i][j] = matriz_identidad[i][j] / pivote
            # Hacer ceros en el resto de la columna para las demás filas
            for fila_actual in range(filas):
                if fila_actual != i:
                    factor_multiplicador = matriz_copia[fila_actual][i]
                    for j in range(columnas):
                        matriz_copia[fila_actual][j] = matriz_copia[fila_actual][j] - (factor_multiplicador * matriz_copia[i][j])
                        matriz_identidad[fila_actual][j] = matriz_identidad[fila_actual][j] - (factor_multiplicador * matriz_identidad[i][j])
        # 4. Redondear los resultados para evitar decimales infinitos muy largos en consola
        for i in range(filas):
            for j in range(columnas):
                matriz_identidad[i][j] = round(matriz_identidad[i][j], 3)
        # Guardar la matriz identidad (que ahora es la inversa) en el resultado
        self.resultado = matriz_identidad