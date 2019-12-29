from pathlib import Path
import random
import io
import os

def generar_pares(a,b):
    if a > b:
        a,b = b,a
    pares = [(x, y) for x in range(a,b) for y in range(a,b) if x != y]
    return pares

def exportar_pares(data, nombre_archivo):
    directorio = os.curdir
    fichero = directorio + "\\" + nombre_archivo + ".txt"
    f = open(fichero, "w", encoding="utf-8")
    f.write(data)
    
        

def menu():
    print("\nGENERADOR DE PARES ALEATORIOS DE NUMEROS")
    print("\nMENU")
    print("Seleccione el número de la opción que desea y presione enter")
    print("1. Generar pares de números automáticamente.")
    print("2. Generar pares de números manualmente.")
    #print("3. Exportar para imprimir.")
    print("4. Salir.")
    print()


menu()
n = int(input())

while n != 4:
    if n == 1:
        c = int(input("\n¿Qué cantidad de pares quiere generar?: "))
        intervalo = input("\nInserte separado por una coma el intervalo entre los cuales lo desea: ")
        li = intervalo.split(',')
        li_enteros = []
        
        for i in li:
            li_enteros.append(int(i))
        li_enteros.sort()
        
        p = generar_pares(li_enteros[0], li_enteros[1])
        result = random.choices(p, k=c)
        para_imprimir = ''
        
        for i in result:
            para_imprimir += str(i) + '\n'
        exportar_pares(para_imprimir, "pares_aleatorios")
        
        print("\nLos números se han generado y exportados al fichero myfile.txt.")
        menu()
        n = int(input('\nInserte la próxima opción que desea: '))

    elif n == 2:
        c = int(input("\n¿Qué cantidad de pares quiere generar?: "))
        intervalo = input("\nInserte separado por una coma el intervalo entre los cuales los desea: ")
        li = intervalo.split(',')
        li_enteros = []

        for i in li:
            li_enteros.append(int(i))
        li_enteros.sort()

        lista_pares = []
        print("\nInserte los números con los cuales quiere formar los pares separados por coma:")
        print("Tenga en cuenta que tiene que estar en el intervalo: [" + str(li_enteros[0]) + ", " + str(li_enteros[1]) +"].")
        entrada = input()
        entradas = entrada.split(',')
        entradas_enteros = []
        for i in range(len(entradas)):
            entradas_enteros.append(int(entradas[i]))
        
        cantidad = len(entradas_enteros)
        if cantidad**2 - cantidad <= c:
            print("La cantidad de números insertados no son suficientes. Vuelva a empezar.")
        else:
            #for j in range(c):
                #a = random.randint(0,len(entradas_enteros)-1)
                #b = random.randint(0,len(entradas_enteros)-1)
            lista_pares = [(x,y) for x in entradas_enteros for y in entradas_enteros if x != y]
            result = random.choices(lista_pares, k=c)                
                        
            para_imprimir = ''
            for i in result:
                para_imprimir += str(i) + '\n'
            exportar_pares(para_imprimir, "pares_manuales")

            print("\nLos números se han generado y exportados al fichero manuales.txt.")
            menu()
            n = int(input('\nInserte la próxima opción que desea: '))



