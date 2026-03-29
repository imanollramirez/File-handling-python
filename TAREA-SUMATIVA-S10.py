# Desarrolla un programa en Python que permita registrar información de estudiantes y guardarla en un archivo de texto.

# 1- Solicitar al usuario los siguientes datos:

# Nombre del estudiante
# Edad
# Carrera o curso
# Promedio de notas

# 2- Guardar la información ingresada en un archivo llamado estudiantes.txt.
# 3- Cada estudiante debe guardarse en una nueva línea con el siguiente formato:

import csv
import os

print('***************************************************')
print('                   BIENVENIDO/A                    ')
print('                Registro de datos                  ')
print('***************************************************')

def validar_carpeta (ruta):
    ruta_actual = os.getcwd()
    path = os.path.join(ruta_actual,ruta)

    if not os.path.exists(path):
        os.mkdir(path)


def guardar_datos(ruta, contenido):
    with open(ruta,'a',newline='',encoding='utf-8') as archivo:
        archivo.write(f'{contenido}\n')

carpeta = "Archivos"
archivo = f'{carpeta}/estudiantes.txt'
validar_carpeta(carpeta)

def datos_estudiante():
    print('---------------------------------------------------')

    contenido = ''

    nombre_estudiante = input('Ingrese su nombre:')
    edad_estudiante = input('Ingrese su edad: ')
    carrera_estudiante = input('Ingrese el nombre de su carrera: ')
    promedio_notas = input('Ingrese su promedio de notas: ')

    contenido = f'{nombre_estudiante or 'Vacío'} | {edad_estudiante or 'Vacío'} | {carrera_estudiante or 'Vacío'} | {promedio_notas or 'Vacío'}'
       # => Esta función de .count(), basicamente devuelve el numero de la cuenta de la palabra que le hayamos indicado.
       #En este caso, yo queria permitir al menos un dato vacío, pero más de eso no.
    if contenido.count('Vacío') >= 2:
        print('************************************************')
        print('\t\t¡IMPORTANTE!\n\tDebe ingresar los datos completos.')
        print('************************************************')
        
        datos_estudiante()
        return
    else: 
        guardar_datos(archivo,contenido)

    print('¿Desea registrar un nuevo estudiante? (Elija 1-2)\n1. SI\n2.NO')
    opcion = int(input())

    if opcion == 1:
        datos_estudiante()
    else :
        print('¡El archivo "estudiantes.txt" se ha guardado con éxito!')

datos_estudiante()


# nombre_estudiante = input('Ingrese su nombre:')
# edad_estudiante = int(input('Ingrese su edad: '))
# carrera_estudiante = input('Ingrese el nombre de su carrera: ')
# promedio_notas = float(input('Ingrese su promedio de notas: '))
