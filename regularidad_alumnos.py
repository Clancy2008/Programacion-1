#Crear una solucion logica estructurada en python usando arreglos, registros y funcoines. para la siguente pregunta.
#¿ Yo quiero saber cuando uno de los siguentes alumnos esta o no esta regular ?
#alumnos = { nombre: "Juan", notas: [7, 8, 9, 6], asistencia: 90 },
#{ nombre: "Maria", notas: [5, 6, 4, 7], asistencia: 60 },
#{ nombre: "Pedro", notas: [1, 9, 4, 7], asistencia: 95 },
#{ nombre: "Ana", notas: [6, 5, 7, 8], asistencia: 85 }

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def regular(alumno):
    promedio = calcular_promedio(alumno["notas"])
    # Es regular si tiene promedio >= 6 y asistencia >= 75
    return promedio >= 6 and alumno["asistencia"] >= 75

alumnos = [
    {"nombre": "Juan", "notas": [7, 8, 9, 6], "asistencia": 90},
    {"nombre": "Maria", "notas": [5, 6, 4, 7], "asistencia": 60},
    {"nombre": "Pedro", "notas": [1, 9, 4, 7], "asistencia": 95},
    {"nombre": "Ana", "notas": [6, 5, 7, 8], "asistencia": 85}
]

# 3. Recorrer la lista e imprimir resultados
for alumno in alumnos:
    promedio = calcular_promedio(alumno["notas"])
    
    if regular(alumno):
        estado = "REGULAR"
    else:
        estado = "NO REGULAR"
        
    print(f"{alumno['nombre']} - Promedio: {promedio:.2f} - Asistencia: {alumno['asistencia']}% -> {estado}")