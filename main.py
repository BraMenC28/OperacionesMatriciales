##pocisiones=[[0 for _ in range (6)] for _ in range (10)]
##print(pocisiones)
##

##array=[[0] * columnas for _ in range (filas) ]
##print(array)

##////////////////// tambien sirve pero es muy largo, es mejor usar el que se puso en la funcion
##matriz=[]
##for _ in range (filas):
##    fil=[]
##    for _ in range (columnas):
##        fil.append(0)
##    matriz.append(fil)
##    #print(fil)///////////
from OperBacicas import OpBasicas
matrizes=OpBasicas(0,0,0)

def llamar_matriz(matriz):## "matriz" es el llamado de las listas que quiera mostrar y que desarrolla la funcion
    for i in matriz:## recorre la lista que se llamo para la funcion(el uso de "in rage()" obliga que sea numeros por eso no se usa)
        print(*i)##para limpiar en consola las comas"," y corchetes "[]"


print("\n \t\t\t---Calculos para matrices---\t\t\n")

filas_1=int(input("\nIngrese el numero de filas de la matriz numero 1: "))
columnas_1=int(input("Ingrese el numero de columnas de la matriz numero 1: "))

matrizes.matriz_1 = [[0 for _ in range(columnas_1)] for _ in range(filas_1)]##se crea la matriz con los datos ingresados. (no importa el indice solo que gire por eso el "_")
llamar_matriz(matrizes.matriz_1)##matriz sin valores y con los arreglos visuales

for i in range(filas_1):
    for j in range (columnas_1):
        matrizes.matriz_1[i][j]=int(input(f"Ingrese el valor de la fila [{i+1}]columna [{j+1}] :"))#ingreso de valores en las posiciones indicadas
print(matrizes.matriz_1)#matriz con los valores pero sin arreglos visuales
llamar_matriz(matrizes.matriz_1)#envia la matriz con los valores para que se arregle la parte visual



filas_2=int(input("\nIngrese el numero de filas de la matriz numero 2: "))
columnas_2=int(input("Ingrese el numero de columnas de la matriz numero 2: "))



matrizes.matriz_2= [[0 for _ in range(columnas_2)] for _ in range(filas_2)]
llamar_matriz(matrizes.matriz_2)

for i in range(filas_2):
    for j in range (columnas_2):
        matrizes.matriz_2[i][j]=int(input(f"Ingrese el valor de la fila [{i+1}]columna [{j+1}] :"))
print(matrizes.matriz_2)
llamar_matriz(matrizes.matriz_2)
print("")

if filas_1==filas_2 and columnas_1==columnas_2:
    matrizes.sumaMatriz(filas_1, columnas_2)
    matrizes.getResultado()
else:
    print("Las matrices no coninciden en sus indices, coindicion para ser sumadas")

matrizes.Multiplicar(filas_1, columnas_1, filas_2, columnas_2)
matrizes.getResultado()


