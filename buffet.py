
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]


def inicializar_catalogo() -> dict:
    """Retorna el catálogo inicial de productos."""
    return {
        101: {"nombre": "Café con leche", "precio": 1500},
        102: {"nombre": "Medialuna", "precio": 700},
        103: {"nombre": "Sándwich de miga", "precio": 1800},
        104: {"nombre": "Agua mineral 500 ml", "precio": 1000},
        105: {"nombre": "Empanada", "precio": 1200},
        106: {"nombre": "Chipá (100 g)", "precio": 1300}
    }

def inicializar_matriz_ventas(num_dias: int, num_productos: int) -> list:
    """Crea una matriz de ceros para almacenar las unidades vendidas por día y producto."""
    return [[0 for _ in range(num_productos)] for _ in range(num_dias)]

def registrar_venta(ventas: list, catalogo: dict, codigos: list):
    """Procedimiento para registrar una venta solicitando datos al usuario."""
    print("\n--- REGISTRAR VENTA ---")
    print("1: Lunes | 2: Martes | 3: Miércoles | 4: Jueves | 5: Viernes")
    dia = int(input("Ingrese día (1-5): ")) - 1
    
    if dia < 0 or dia > 4:
        print("Error: Día inválido.")
        return

    codigo = int(input("Ingrese código del producto: "))
    if codigo not in catalogo:
        print("Error: El producto no existe en el catálogo.")
        return

    cantidad = int(input("Ingrese cantidad vendida: "))
    if cantidad <= 0:
        print("Error: La cantidad debe ser mayor a 0.")
        return

    # Mapeo de código a índice de la matriz
    idx_prod = codigos.index(codigo)
    ventas[dia][idx_prod] += cantidad
    print(f"-> Venta registrada: {cantidad} x {catalogo[codigo]['nombre']} para el día {DIAS[dia]}.")

def calcular_unidades_por_producto(ventas: list, idx_prod: int) -> int:
    """Calcula el total de unidades vendidas de un producto a lo largo de la semana."""
    total = 0
    for dia in range(len(ventas)):
        total += ventas[dia][idx_prod]
    return total

def calcular_recaudacion_dia(ventas: list, catalogo: dict, codigos: list, dia: int) -> float:
    """Calcula la recaudación total de un día específico."""
    recaudacion = 0.0
    for idx_prod, codigo in enumerate(codigos):
        unidades = ventas[dia][idx_prod]
        precio = catalogo[codigo]["precio"]
        recaudacion += unidades * precio
    return recaudacion

def mostrar_informes(ventas: list, catalogo: dict, codigos: list):
    """Procedimiento para generar y mostrar todos los informes requeridos por Marta."""
    print("           INFORMES DE VENTAS DE LA SEMANA         ")
    

    # 1. Unidades vendidas por producto
    print("\n1. UNIDADES VENDIDAS POR PRODUCTO:")
    totales_por_prod = []
    for idx, codigo in enumerate(codigos):
        total_prod = calcular_unidades_por_producto(ventas, idx)
        totales_por_prod.append(total_prod)
        print(f" - {catalogo[codigo]['nombre']}: {total_prod} unidades")

   
    print("\n2. RECAUDACIÓN POR DÍA:")
    recaudaciones_dias = []
    recaudacion_total = 0.0
    for d in range(len(DIAS)):
        rec_dia = calcular_recaudacion_dia(ventas, catalogo, codigos, d)
        recaudaciones_dias.append(rec_dia)
        recaudacion_total += rec_dia
        print(f" - {DIAS[d]}: ${rec_dia:,.2f}")

    
    max_unidades = max(totales_por_prod)
    if max_unidades > 0:
        mas_vendidos = [catalogo[codigos[i]]["nombre"] for i, cant in enumerate(totales_por_prod) if cant == max_unidades]
        print(f"\n3. PRODUCTO(S) MÁS VENDIDO(S): {', '.join(mas_vendidos)} ({max_unidades} unidades)")
    else:
        print("\n3. PRODUCTO MÁS VENDIDO: No se registraron ventas.")

    max_rec = max(recaudaciones_dias)
    if max_rec > 0:
        dias_max = [DIAS[i] for i, rec in enumerate(recaudaciones_dias) if rec == max_rec]
        print(f"   DÍA DE MAYOR RECAUDACIÓN: {', '.join(dias_max)} (${max_rec:,.2f})")
    else:
        print("   DÍA DE MAYOR RECAUDACIÓN: No hubo ingresos.")

  
    no_vendidos = [catalogo[codigos[i]]["nombre"] for i, cant in enumerate(totales_por_prod) if cant == 0]
    print("\n4. PRODUCTOS SIN VENTAS:")
    if no_vendidos:
        for p in no_vendidos:
            print(f" - {p}")
    else:
        print(" - Todos los productos registraron al menos una venta.")

    # 5. Recaudación total de la semana
    print(f"\n5. RECAUDACIÓN TOTAL DE LA SEMANA: ${recaudacion_total:,.2f}")
    print("==================================================\n")

def cargar_datos_prueba_cuaderno(ventas: list, codigos: list):
    """Procedimiento utilitario para precargar los datos ficticios del cuaderno."""
    # Lunes
    ventas[0][codigos.index(101)] = 30
    ventas[0][codigos.index(102)] = 40
    ventas[0][codigos.index(103)] = 10
    ventas[0][codigos.index(104)] = 20
    ventas[0][codigos.index(105)] = 15
    # Martes
    ventas[1][codigos.index(101)] = 25
    ventas[1][codigos.index(102)] = 38
    ventas[1][codigos.index(103)] = 12
    ventas[1][codigos.index(104)] = 22
    # Miércoles
    ventas[2][codigos.index(101)] = 28
    ventas[2][codigos.index(102)] = 45
    ventas[2][codigos.index(103)] = 8
    ventas[2][codigos.index(104)] = 18
    ventas[2][codigos.index(105)] = 20
    # Jueves
    ventas[3][codigos.index(101)] = 35
    ventas[3][codigos.index(102)] = 50
    ventas[3][codigos.index(103)] = 15
    ventas[3][codigos.index(104)] = 25
    ventas[3][codigos.index(105)] = 18
    # Viernes
    ventas[4][codigos.index(101)] = 20
    ventas[4][codigos.index(102)] = 30
    ventas[4][codigos.index(103)] = 9
    ventas[4][codigos.index(104)] = 30
    ventas[4][codigos.index(105)] = 25
    print("-> Datos del cuaderno cargados exitosamente.")



def main():
    catalogo = inicializar_catalogo()
    codigos_ordenados = sorted(catalogo.keys())
    ventas = inicializar_matriz_ventas(len(DIAS), len(codigos_ordenados))

    while True:
        print("\n=== MENU BUFFET FACULTAD ===")
        print("1. Registrar una venta")
        print("2. Ver informes semanales")
        print("3. Cargar datos del cuaderno (Prueba)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta(ventas, catalogo, codigos_ordenados)
        elif opcion == "2":
            mostrar_informes(ventas, catalogo, codigos_ordenados)
        elif opcion == "3":
            cargar_datos_prueba_cuaderno(ventas, codigos_ordenados)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()