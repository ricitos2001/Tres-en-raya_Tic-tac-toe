# -*- coding: utf-8 -*-
import random
import os
import sys

AZUL = "\33[34m"
ROJO = "\33[31m"
VERDE = "\33[32m"
AMARILLO = '\033[1;93m'
NARANJA = '\33[33m'
MAGENTA = "\033[1;035m"
CIAN = "\033[36m"
GRIS = "\033[1;90m"
BLANCO = "\033[1;39m"
RESETEO = '\033[0m'

def borrar_consola():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def checkear_version_de_python():
    version_requerida = [(3, 10), (3, 11), (3, 12)]
    version_instalada = sys.version_info[:2]
    if version_instalada in version_requerida:
        verificacion="version de python: "+str(version_instalada)+"\nla version de python instalada es compatible."
        print(verificacion)
        os.system("pause")
        borrar_consola()
    else:
        verificacion="la version de python instalada es compatible\nes necesario tener instalado Python3.10, 3.11, o 3.12"
        print(verificacion)

#impresion del rablero
def imprimir_tablero(tablero):
    print(" --- --- --- ")
    for fila in tablero[:-1]:
        print("| "+" | ".join(fila)+" |")
        print(" --- --- --- ")
    print("| "+" | ".join(tablero[-1])+" |\n --- --- --- ")

# turno del jugador
def introducir_coordenadas_fila():
    mensaje_error="solo se permite introducir un numero del 1 al 3 asi que por favor intentalo de nuevo"
    numero = 0
    while numero<=0:
        try:
            numero = int(input("introduzca una coordenada para la fila que sea del 1 al 3: "))
            if numero in [1, 2, 3]:
                return numero
        except ValueError:
            print(mensaje_error)

def introducir_coordenadas_columna():
    mensaje_error="solo se permite introducir un numero del 1 al 3 asi que por favor intentalo de nuevo"
    numero = 0
    while numero<=0:
        try:
            numero = int(input("introduzca una coordenada para la columna que sea del 1 al 3: "))
            if numero in [1, 2, 3]:
                return numero
        except ValueError:
            print(mensaje_error)

# comprobar la posicion del jugador
def posicion_jugador(tablero):
    fila = introducir_coordenadas_fila()
    columna = introducir_coordenadas_columna()
    while tablero[fila - 1][columna - 1] != "-":
        fila = introducir_coordenadas_fila()
        columna = introducir_coordenadas_columna()
    tablero[fila - 1][columna - 1] = AZUL + "X" + RESETEO
    return tablero

# turno de la maquina
def posicion_maquina(tablero):
    fila = random.randint(0, 2)
    columna = random.randint(0, 2)
    while tablero[fila][columna] != "-":
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
    tablero[fila][columna] = ROJO + "O" + RESETEO
    return tablero

# verificar si hay victoria, derrota o empate
def verificar_victoria(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if fila.count(jugador) == 3:
            return True
    # Verificar columnas
    for j in range(3):
        for i in range(3):
            if tablero[i][j] != jugador:
                break
        else:
            return True
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False

if __name__ == "__main__":
    #entrada
    checkear_version_de_python()
    tablero = [["-","-","-"],["-","-","-"],["-","-","-"]]
    #proceso
    borrar_consola()
    inicio = ("----------------------------------------------------------TRES EN RAYA!----------------------------------------------------------\nINSTRUCCIONES:\n1.) el jugador debe introducir un nombre\n2.) para marcar las coordenadas el jugador debera introducir tanto para las filas como para las columnas un numero del 1 al 3 y cuando se introduzcan los dos numeros estos se multiplicaran y dependiendo del resultado se imprimira una X en una de las casillas del tablero\n3.) las casillas del tablero vienen representadas por una serie de numeros del 1 al 9:\n --- --- --- \n| 1 | 2 | 3 |\n --- --- --- \n| 4 | 5 | 6 |\n --- --- --- \n| 7 | 8 | 9 |\n --- --- --- \n4.) de manera instantanea el NPC imprimira una Y\n5.) no se pueden introducir numeros que sean menores que 1 o mayores que 3\n6.) no se pueden introducir letras\n7.) no se pueden introducir numeros cuyas casillas ya estan ocupadas por una X o una Y\n8.) si por casualidad introducese un numero menor que 1 o mayor que 10 o introduces un numero cuya casilla correspondiente ha sido ocupada por una X o una Y se repetira el turno del jugador\n---------------------------------------------------------------------------------------------------------------------------------")
    print(inicio)
    nombre = input("introduce el nombre del jugador: ")
    ejecucion = True
    while ejecucion:
        borrar_consola()
        imprimir_tablero(tablero)
        impresion = posicion_jugador(tablero)
        # Verificar si el jugador ha ganado
        if verificar_victoria(tablero,AZUL + "X" + RESETEO):
            borrar_consola()
            imprimir_tablero(tablero)
            mensaje = VERDE + nombre + " gana, NPC pierde...\n" + AMARILLO + "henorabuena!\nhas ganado 🏆" + RESETEO + "\n"
            print(mensaje)
            continuar=input(BLANCO + "pulse cualquier tecla para para cerrar la partida: " + RESETEO)
            borrar_consola()
            ejecucion = False
        # Verificar si hay un empate
        elif all(all(casilla != "-" for casilla in fila) for fila in tablero):
            borrar_consola()
            imprimir_tablero(tablero)
            mensaje = CIAN + "empate...\n"+ GRIS + "A MIMIR! 😴😴😴😴😴" + RESETEO + "\n"
            print(mensaje)
            continuar=input(BLANCO + "pulse cualquier tecla para para cerrar la partida: " + RESETEO)
            borrar_consola()
            ejecucion = False
        else:
            impresion = posicion_maquina(tablero)
        # Verificar si el jugador ha perdido
        if verificar_victoria(tablero,ROJO+"O"+RESETEO):
            borrar_consola()
            imprimir_tablero(tablero)
            mensaje = NARANJA +  nombre + " pierde, NPC gana...\n" + MAGENTA + "has perdido!\nPIPIPI PIPIPI 😱" + RESETEO + "\n"
            print(mensaje)
            continuar=input(BLANCO + "pulse cualquier tecla para para cerrar la partida: " + RESETEO)
            borrar_consola()
            ejecucion = False
