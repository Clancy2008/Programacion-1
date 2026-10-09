import json


def calcular_promedio(notas):
    return sum(notas) / len(notas)

def es_regular(alumno):
    promedio = calcular_promedio(alumno["notas"])
    return promedio >= 6 and alumno["asistencia"] >= 75


datos_alumnos = [
    {"nombre": "Juan", "notas": [7, 8, 9, 6], "asistencia": 90},
    {"nombre": "Maria", "notas": [5, 6, 4, 7], "asistencia": 60},
    {"nombre": "Pedro", "notas": [1, 9, 4, 7], "asistencia": 95},
    {"nombre": "Ana", "notas": [6, 5, 7, 8], "asistencia": 85}
]


with open("alumnos.json", "w") as archivo:
    json.dump(datos_alumnos, archivo, indent=4)


with open("alumnos.json", "r") as archivo:
    alumnos = json.load(archivo)


for alumno in alumnos:
    promedio = calcular_promedio(alumno["notas"])
    estado = "REGULAR" if es_regular(alumno) else "NO REGULAR"
    print(f"{alumno['nombre']} - Promedio: {promedio:.2f} - Asistencia: {alumno['asistencia']}% -> {estado}")