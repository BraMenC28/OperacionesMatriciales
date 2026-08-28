from Operaciones import OpBasicas
from Ordenamiento import Ordenamiento
matrizes=OpBasicas(0,0,0)

def llamar_matriz(matriz):## "matriz" es el llamado de las listas que quiera mostrar y que desarrolla la funcion
    for i in matriz:## recorre la lista que se llamo para la funcion(el uso de "in rage()" obliga que sea numeros por eso no se usa)
        print(*i)##para limpiar en consola las comas"," y corchetes "[]"


print("\n \t\t\t---Calculos para matrices---\t\t\n")


elecion=0
while(elecion!=6):
    elecion=int(input("\n\t Porfavor elija una de las operaciones a realizar\n\n 1. Suma de Matrices\n 2. Multiplicacion de matrices \n 3. Inversa de matrices \n 4. Multiplicacion matriz-vector\n 5. Orgranizacion de matriz \n 6. Salir\n   -> "))
    match (elecion):
        case 1:
            filas_1=int(input("\nIngrese el numero de filas de la matriz numero 1: "))
            columnas_1=int(input("Ingrese el numero de columnas de la matriz numero 1: "))
            matrizes.matriz_1 = [[0 for _ in range(columnas_1)] for _ in range(filas_1)]##se crea la matriz con los datos ingresados. (no importa el indice solo que gire por eso el "_")
            #llamar_matriz(matrizes.matriz_1)##matriz sin valores y con los arreglos visuales

            for i in range(filas_1):
                for j in range (columnas_1):
                    matrizes.matriz_1[i][j]=int(input(f"Ingrese el valor de la fila [{i+1}]columna [{j+1}] :"))#ingreso de valores en las posiciones indicadas
            #print(matrizes.matriz_1)#matriz con los valores pero sin arreglos visuales
            print("\nMatriz_1 ingresada: ")
            llamar_matriz(matrizes.matriz_1)#envia la matriz con los valores para que se arregle la parte visual

            filas_2=int(input("\nIngrese el numero de filas de la matriz numero 2: "))
            columnas_2=int(input("Ingrese el numero de columnas de la matriz numero 2: "))
            matrizes.matriz_2= [[0 for _ in range(columnas_2)] for _ in range(filas_2)]
            #llamar_matriz(matrizes.matriz_2)##matriz en ceros y sin valores

            for i in range(filas_2):
                for j in range (columnas_2):
                    matrizes.matriz_2[i][j]=int(input(f"Ingrese el valor de la fila [{i+1}]columna [{j+1}] :"))
            #print(matrizes.matriz_2)#matriz sin arreglos
            print("\nMatriz_2 ingresada: ")
            llamar_matriz(matrizes.matriz_2)
            print("")

            if filas_1==filas_2 and columnas_1==columnas_2:
                matrizes.sumaMatriz(filas_1, columnas_1)
                print("\nEl resultado de la matriz es: ")
                matrizes.getResultado()
            else:
                print("Las matrices no coninciden en sus indices, coindicion para ser sumadas")
        case 2:
            filas_1=int(input("\nIngrese el numero de filas de la matriz numero 1: "))
            columnas_1=int(input("Ingrese el numero de columnas de la matriz numero 1: "))
            matrizes.matriz_1 = [[0 for _ in range(columnas_1)] for _ in range(filas_1)]##se crea la matriz con los datos ingresados. (no importa el indice solo que gire por eso el "_")
            #llamar_matriz(matrizes.matriz_1)##matriz sin valores y con los arreglos visuales

            for i in range(filas_1):
                for j in range (columnas_1):
                    matrizes.matriz_1[i][j]=int(input(f"Ingrese el valor de la fila [{i+1}]columna [{j+1}] :"))#ingreso de valores en las posiciones indicadas
            #print(matrizes.matriz_1)#matriz con los valores pero sin arreglos visuales
            print("\nMatriz_1 ingresada: ")
            llamar_matriz(matrizes.matriz_1)#envia la matriz con los valores para que se arregle la parte visual

            filas_2=int(input("\nIngrese el numero de filas de la matriz numero 2: "))
            columnas_2=int(input("Ingrese el numero de columnas de la matriz numero 2: "))
            matrizes.matriz_2= [[0 for _ in range(columnas_2)] for _ in range(filas_2)]
            #llamar_matriz(matrizes.matriz_2)

            for i in range(filas_2):
                for j in range (columnas_2):
                    matrizes.matriz_2[i][j]=int(input(f"Ingrese el valor de la fila [{i+1}]columna [{j+1}] :"))
            #print(matrizes.matriz_2)#matriz sin arreglo
            llamar_matriz(matrizes.matriz_2)
            print("")

            if columnas_1==filas_2:
                matrizes.Multiplicar(filas_1, columnas_1, filas_2, columnas_2)
                matrizes.getResultado()
            else:
                print("No coinciden los indices para la operacion de multiplicacion ([m x n] * [n x p])")
        case 3:
            print("falta")
        case 4:
            filas_1=int(input("\nIngrese el numero de filas de la matriz numero 1: "))
            columnas_1=int(input("Ingrese el numero de columnas de la matriz numero 1: "))
            matrizes.matriz_1 = [[0 for _ in range(columnas_1)] for _ in range(filas_1)]##se crea la matriz con los datos ingresados. (no importa el indice solo que gire por eso el "_")
            #llamar_matriz(matrizes.matriz_1)##matriz sin valores y con los arreglos visuales

            for i in range(filas_1):
                for j in range (columnas_1):
                    matrizes.matriz_1[i][j]=int(input(f"Ingrese el valor de la fila [{i+1}]columna [{j+1}] :"))#ingreso de valores en las posiciones indicadas
            #print(matrizes.matriz_1)#matriz con los valores pero sin arreglos visuales
            print("\nMatriz_1 ingresada: ")
            llamar_matriz(matrizes.matriz_1)#envia la matriz con los valores para que se arregle la parte visual

            filas_2=int(input("\nIngrese el numero de filas del vector : "))
            columnas_2=1
            matrizes.matriz_2= [[0 for _ in range(columnas_2)] for _ in range(filas_2)]
            #llamar_matriz(matrizes.matriz_2)#matriz en ceros y con arreglo

            for i in range(filas_2):
                for j in range (columnas_2):
                    matrizes.matriz_2[i][j]=int(input(f"Ingrese el valor de la fila [{i+1}]columna [{j+1}] :"))
            #print(matrizes.matriz_2)#con valores sin arreglo
            print("\nVector ingresado: ")
            llamar_matriz(matrizes.matriz_2)
            print("")
            if columnas_1==filas_2:
                matrizes.Multiplicar(filas_1, columnas_1, filas_2, columnas_2)
                matrizes.getResultado()
            else:
                print("No coinciden los indices para la operacion de multiplicacion ([m x n] * [n x p])")
        case 5:
            cantidad=int(input("ingrese el tamaño del vector a ordenar\n"))
            objeto = Ordenamiento(cantidad)
            print("Que metodo de ordenamiento desea usar?""\n 1.Burbuja\n 2.Inserccion\n 3.Seleccion\n 4.Mergesort")
            opcion = int(input("Ingrese una opción: "))
            match opcion:
                case 1:
                    print("Escogido el metodo burbuja\n")
                    objeto.burbuja()
                    print("Lista ordenada:")
                    print(objeto.getResultado())

                case 2:
                        print("Escogido el metodo de inserccion\n")
                        objeto.inserccion()
                        print("Lista ordenada:")
                        print(objeto.getResultado())

                case 3:
                        print("Escogido el metodo de seleccion\n")
                        objeto.seleccion()
                        print("Lista ordenada:")
                        print(objeto.getResultado())

                case 4:
                        print("Escogido el metodo mergesort\n")
                        objeto.merge()
                        print("Lista ordenada:")
                        print(objeto.getResultado())
