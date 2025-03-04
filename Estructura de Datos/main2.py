import numpy as np
import random as rn

def generarNombre():
    nombres = ["Ana", "Luis", "Carlos", "Marta", "José", "Lucía", "Pedro", "María", "Santiago", "Laura",
    "Antonio", "Isabel", "Javier", "Paula", "Manuel", "Carmen", "Francisco", "Elena", "Raúl", "Sofía",
    "David", "Pilar", "Andrés", "Sara", "José Luis", "Beatriz", "Tomás", "Natalia", "Miguel", "Raquel",
    "Fernando", "Teresa", "Álvaro", "Nuria", "Diego", "Celia", "Eduardo", "Inés", "Ricardo", "Adriana",
    "Juan", "Esteban", "Verónica", "Rocío", "Enrique", "Gloria", "Sergio", "Marina", "Víctor", "Alicia"]

    apellidos = ["González", "Rodríguez", "López", "Martínez", "Hernández", "Pérez", "Gómez", "Sánchez", "Ramírez", "Torres",
    "Álvarez", "Díaz", "Ruiz", "Jiménez", "Muñoz", "Moreno", "Serrano", "Molina", "Vázquez", "Castro",
    "Ramón", "Fernández", "Jiménez", "Morales", "Vega", "Cordero", "Sanz", "Navarro", "Ríos", "Gutiérrez",
    "Méndez", "Gil", "Cano", "Carrillo", "Suárez", "Luna", "Cortés", "Paredes", "Campos", "Villar",
    "Pons", "Solís", "Rojas", "Castilla", "Prieto", "Díaz", "Ramos", "Montero", "Blanco", "Nieto"]

    nombre = nombres[rn.randint(0, 49)] + " " + apellidos[rn.randint(0, 49)]
    return nombre

def diccionarioCarreras(x):
    carreras_uis = [
        "Ingeniería de Sistemas",
        "Ingeniería Civil",
        "Ingeniería Eléctrica",
        "Ingeniería Electrónica",
        "Ingeniería Industrial",
        "Ingeniería Mecánica",
        "Diseño Industrial",
        "Economía",
        "Filosofía",
        "Ingeniería Metalúrgica"
    ]

    return carreras_uis[x]


n_estudiantes = 6500

estudiante = []
codigo = 2241000

for i in range(n_estudiantes):
    #Código, nombre, promedio, carrera, año ingreso

    estudiante.append([codigo, generarNombre(), round(rn.uniform(2.8, 5), 2), rn.randint(0, 9), rn.randint(1980, 2025)])
    codigo += 1


def main(entrada):

    #----- 1 -----
    if entrada == 1:

        cantidad = 0
        codigo_carrera = int(input("Ingrese el código de la carrera que desea buscar (0 - 9): "))
            
        for i in range(len(estudiante) - 1):
            if (estudiante[i][3] == codigo_carrera) and (estudiante[i][2] >= 4):

                cantidad += 1
                print(f"{cantidad}. {estudiante[i][0]}, {estudiante[i][1]}")
                
        print(f"\nEstudiantes de {diccionarioCarreras(codigo_carrera)} con promedio igual o mayor a 4.0")
        print(f"Total: {cantidad}")


    #----- 2 -----
    elif entrada == 2:
        cantidad1 = 0
        for i in range(len(estudiante) - 1):
            if (estudiante[i][4] < 1990) and (estudiante[i][2] <= 3.2):
                
                cantidad1 += 1
                print(f"{cantidad1}. {estudiante[i][0]}, {estudiante[i][1]}")

        print(f"\nEstudiantes que ingresaron antes de 1990 y están condicionales")
        print(f"Total: {cantidad1}")

    else:
        print("Ingrese 1 o 2")

# -----------------------------------------------------------

print("\nSeleccione el ejercicio a imprimir(1 o 2)")
entrada = int(input())
main(entrada)