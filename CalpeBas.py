##pocisiones=[[0 for _ in range (6)] for _ in range (10)]
##print(pocisiones)
##

##array=[[0] * columnas for _ in range (filas) ]
##print(array)

print("\n \t\t\t---Calculos para matrices---\t\t\n")
filas=int(input("\nIngrese el numero de filas de la matriz: "))
columnas=int(input("Ingrese el numero de columnas de la matriz: "))


##////////////////// tambien sirve pero es muy largo, es mejor usar el que se puso en la funcion
##matriz=[]
##for _ in range (filas):
##    fil=[]
##    for _ in range (columnas):
##        fil.append(0)
##    matriz.append(fil)
##    #print(fil)///////////


def llamar_matriz(matriz):## "matriz" es el llamado de las listas que quira mostrar y que desarrolla la funcion
    for i in matriz:## recorre la lista que se llamo para la funcion(el uso de "in rage()" obliga que sea numeros por eso no se usa)
        print(*i)##para limpiar en consola las comas"," y corchetes "[]"
matriz = [[0 for _ in range(columnas)] for _ in range(filas)]##se crea la matriz con los datos ingresados. (no importa el indice solo que gire por eso el "_")
llamar_matriz(matriz)