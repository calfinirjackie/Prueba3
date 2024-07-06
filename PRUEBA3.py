import csv
global lista 
global nombrearchivo
lista = [ 
    ["rut","nombre","Nota 1","Nota 2"], 
    ["12.345.678-9","Ana Martinez",6.0,5.5],
    ["98.765.432-1","Juan Perez",7.0,6.5],
    ["13.579.246-8","Maria Gonzalez",4.5,5.0],
    ["24.681.357-9","Pedro Ramirez",6.5,6.0],
    ["31.415.926-5","Laura Fernandez",5.5,5.0],
    ["27.182.818-2","Luis Morales",6.0,5.5],
    ["11.223.344-5","Carmen Rojas",7.0,6.5],
    ["55.667.788-9","Jorge Contreras",5.0,4.5],
    ["99.887.766-5","Sofia Valenzuela",6.5,6.0],
    ["44.332.211-0","Francisco Vargas",5.5,5.0],
    ["66.778.899-0","Valentina Castillo",6.0,5.5],
    ["12.349.876-5","Nicolas Reyes",7.0,6.5],
    ["87.654.321-0","Gabriela Munoz",4.5,5.0],
    ["14.253.647-8","Cristian Soto",6.5,6.0],
    ["36.473.829-1","Daniela Silva",5.5,5.0],
    ["19.283.746-5","Pablo Sandoval",6.0,5.5],
    ["45.678.912-3","Margarita Espinoza",7.0,6.5],
    ["67.890.543-2","Esteban Fuentes",5.0,4.5],
    ["34.567.890-1","Alicia Carrasco",6.5,6.0],
    ["90.817.263-4","Mateo Henriquez",5.5,5.0],
    ["76.543.210-9","Antonia Figueroa",6.0,5.5],
    ["87.456.312-4","Jose Navarro",7.0,6.5],
    ["29.837.465-0","Rocio Araya",4.5,5.0],
    ["43.829.012-5","Felipe Aguirre",6.5,6.0],
    ["98.712.345-6","Camila Pizarro",5.5,5.0]
    ]

nombrearchivo = "ListaCurso5B.csv"

def opcion1():
    with open('ListaCurso5B.csv', 'r', newline="") as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            lista.append(fila)

    print("Información del curso:")
    for fila in lista:
        print(fila)

def opcion2():
    print("Ingrese los siguientes datos para ingresar al estudiante")
    rut = input("Ingrese RUT del estudiante: ")
    nombreestudiante = input("Ingrese Nombre del estudiante: ")
    Apellidoestudiante = input("Ingrese Apellido del estudiante: ")
    nota1 = input("Ingrese Nota 1 del estudiante: ")
    nota2 = input("ingrese Nota 2 del estudiante: ")

    alumnonuevo = {"rut": rut,
                   "nombre" : nombreestudiante,
                   "apellido" : Apellidoestudiante,
                   "nota1" : nota1,
                   "nota 2" : nota2}
    
    lista.append(alumnonuevo)
   
def opcion3():
    print("Modificar Nota")
    rutestudiante = input("Ingrese el RUT del estudiante: ")
    print("Ingrese si desea modificar 1. Nota 1 o 2. Nota 2")
    opcnota = int(input(" Ingrese opción 1 0 2: "))
    notamodificada = float(input("Ingrese la nueva nota: "))

    if opcnota == 1:
        print("Nota 1 modificada")
        

    if opcnota == 2:
        print("Nota 2 modificada")
        

    else:
        ("Ingrese opción correcta, 1 o 2")

def opcion4():
    print("Eliminar Estudiante")
    eliminarestudiante = input("Ingrese RUT del estudiante a eliminar: ")
    isaliminarestudiante = input("Está seguro de que desea eliminar al estudiante? (SI/NO): ")
    isaliminarestudiante = isaliminarestudiante.upper
    if isaliminarestudiante == "SI":
        print("Estudiante eliminado correctamente")

    else:
        print("Vuelve al menú principal")

def opcion5():
    print("Generar promedio de notas")
    print("Proceso de generación de promedios finalizado")

def opcion6():
    "Generar Acta de cierre de curso"


def salida():
    print("Está saliendo del programa. Hasta pronto.")

while True:
    print("Estimado/a Bienvenido a su programa de calificaciones de EducandoAndo")
    print("De la lista a continuación, ingrese la opción de 1 - 7 de la acción que desea realizar")
    print("1. Procesar lista de Estudiantes")
    print("2. Registrar Estudiante")
    print("3. Modificar Nota")
    print("4. Eliminar Estudiante")
    print("5. Generar promedio de notas")
    print("6. Generar Acta de Cierre de Curso")
    print("7. Salir")
    opc = int(input("Ingrese opción de 1 - 7: "))

    if opc == 1:
        opcion1()

    if opc == 2:
        opcion2()

    if opc == 3:
        opcion3()

    if opc == 4:
        opcion4()

    if opc == 5:
        opcion5()

    if opc == 6:
        opcion6()

    if opc == 7:
        salida()
        break