def cargar_jugadores():
    jugadores = []

    cantidad = int(input("¿Cuántos jugadores va a cargar? "))

    for i in range(cantidad):
        nombre = input("Ingrese el nombre del jugador: ")
        categoria = input("Ingrese la categoría: ")

        jugadores.append(nombre + ";" + categoria)

    return jugadores


def guardar_jugadores(jugadores):
    archivo = open("jugadores.txt", "w", encoding="utf-8")

    for jugador in jugadores:
        archivo.write(jugador + "\n")

    archivo.close()


def leer_jugadores():
    jugadores = []

    try:
        archivo = open("jugadores.txt", "r", encoding="utf-8")

        for linea in archivo:
            jugadores.append(linea.strip())

        archivo.close()

    except FileNotFoundError:
        print("Todavía no hay jugadores guardados.")

    return jugadores


def agregar_jugador():
    nombre = input("Ingrese el nombre del jugador: ")
    categoria = input("Ingrese la categoría: ")

    archivo = open("jugadores.txt", "a", encoding="utf-8")
    archivo.write(nombre + ";" + categoria + "\n")
    archivo.close()

    print("Jugador agregado correctamente.")


def mostrar_jugadores():
    jugadores = leer_jugadores()

    print("LISTA DE JUGADORES")

    for jugador in jugadores:
        datos = jugador.split(";")
        print("Nombre:", datos[0], "- Categoría:", datos[1])


def buscar_jugador():
    nombre_buscar = input("Ingrese el nombre del jugador que busca: ")
    jugadores = leer_jugadores()
    encontrado = False

    for jugador in jugadores:
        datos = jugador.split(";")

        if datos[0].lower() == nombre_buscar.lower():
            print("Jugador:", datos[0])
            print("Categoría:", datos[1])
            encontrado = True

    if encontrado == False:
        print("El jugador no está inscripto.")


def eliminar_jugador():
    nombre_eliminar = input("Ingrese el nombre del jugador que desea eliminar: ")
    jugadores = leer_jugadores()
    nuevos_jugadores = []
    encontrado = False

    for jugador in jugadores:
        datos = jugador.split(";")

        if datos[0].lower() == nombre_eliminar.lower():
            encontrado = True
        else:
            nuevos_jugadores.append(jugador)

    if encontrado:
        guardar_jugadores(nuevos_jugadores)
        print("Jugador eliminado correctamente.")
    else:
        print("El jugador no está inscripto.")


def main():
    opcion = ""

    while opcion != "6":
        print("\n--- TORNEO DE PADEL ---")
        print("1. Cargar jugadores")
        print("2. Agregar un jugador")
        print("3. Mostrar jugadores")
        print("4. Buscar jugador")
        print("5. Eliminar jugador")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugadores = cargar_jugadores()
            guardar_jugadores(jugadores)
            print("Jugadores guardados correctamente.")

        elif opcion == "2":
            agregar_jugador()

        elif opcion == "3":
            mostrar_jugadores()

        elif opcion == "4":
            buscar_jugador()

        elif opcion == "5":
            eliminar_jugador()

        elif opcion == "6":
            print("Programa finalizado.")

        else:
            print("Opción incorrecta.")

main()