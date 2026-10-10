NOMBRE_ARCHIVO = "ventas_buffet.txt"
DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# --- CATÁLOGO DE PRODUCTOS ---
catalogo_productos = [
    {"codigo": 101, "nombre": "Café con leche", "precio": 1500.0},
    {"codigo": 102, "nombre": "Medialuna", "precio": 700.0},
    {"codigo": 103, "nombre": "Sándwich de miga", "precio": 1800.0},
    {"codigo": 104, "nombre": "Agua mineral 500 ml", "precio": 1000.0},
    {"codigo": 105, "nombre": "Empanada", "precio": 1200.0},
    {"codigo": 106, "nombre": "Chipá (100 g)", "precio": 1300.0}
]

def buscar_posicion_producto(codigo: int) -> int:
    """Función 1: Devuelve la columna (0..5) del producto o -1 si no existe."""
    for pos, producto in enumerate(catalogo_productos):
        if producto["codigo"] == codigo:
            return pos
    return -1

def cargar_ventas_desde_archivo() -> list[list[int]]:
    """Función 2: Lee el archivo .txt o emite alerta si es el primer uso."""
    matriz = [[0 for _ in range(6)] for _ in range(5)]
    
    if os.path.exists(NOMBRE_ARCHIVO):
        try:
            with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
                lineas = f.readlines()
                for i in range(min(5, len(lineas))):
                    valores = lineas[i].strip().split(",")
                    for j in range(min(6, len(valores))):
                        matriz[i][j] = int(valores[j])
            print(f"[INFO] Datos cargados exitosamente desde '{NOMBRE_ARCHIVO}'.")
        except (ValueError, IOError):
            print("[ALERTA] Archivo dañado o corrupto. Se inicializa matriz en 0.")
    else:
        print(f"[ALERTA] El archivo '{NOMBRE_ARCHIVO}' no existe en el directorio.")
        print("[INFO] Se inicia el sistema por primera vez con matriz de ventas en cero (0).\n")
        
    return matriz

def calcular_recaudacion_dia(matriz: list[list[int]], dia_idx: int) -> float:
    """Función 3: Calcula la recaudación en pesos de un día específico."""
    total_dia = 0.0
    for col_idx in range(6):
        unidades = matriz[dia_idx][col_idx]
        precio = catalogo_productos[col_idx]["precio"]
        total_dia += unidades * precio
    return total_dia

# ==============================================================================
# SUBPROGRAMAS: PROCEDIMIENTOS
# ==============================================================================

def mostrar_menu():
    """Procedimiento 1: Despliega las opciones del menú."""

    print("      SISTEMA DE GESTIÓN - BUFFET FACULTAD   ")
    
    print("1. Consultar Catálogo de Productos")
    print("2. Registrar Venta Diaria")
    print("3. Generar Informes Consolidados de la Semana")
    print("4. Guardar y Salir del Sistema")
    

def guardar_ventas_en_archivo(matriz: list[list[int]]):
    """Procedimiento 2: Vuelca la matriz al archivo de texto secuencial."""
    try:
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
            for fila in matriz:
                f.write(",".join(map(str, fila)) + "\n")
        print("\n[INFO] Datos de la semana guardados correctamente en disco.")
    except IOError as e:
        print(f"\n[ERROR] No se pudo guardar en disco: {e}")

def generar_informes_semanal(matriz: list[list[int]]):
    """Procedimiento 3: Genera los 5 reportes consolidados requeridos."""
    print("\n INFORME CONSOLIDADO SEMANAL ")

    # 1. Unidades vendidas por producto
    print("\n1. Unidades vendidas por producto:")
    unidades_por_prod = * 6
    for col in range(6):
        unidades_por_prod[col] = sum(matriz[row][col] for row in range(5))
        prod_nombre = catalogo_productos[col]["nombre"]
        print(f"   - {prod_nombre:<22}: {unidades_por_prod[col]} unidades")

    # 2. Recaudación por día
    print("\n2. Recaudación acumulada por día:")
    recaudacion_dias = []
    for fila in range(5):
        rec_dia = calcular_recaudacion_dia(matriz, fila)
        recaudacion_dias.append(rec_dia)
        print(f"   - {DIAS_SEMANA[fila]:<10}: ${rec_dia:,.2f}")

    # 3. Destacados
    max_unidades = max(unidades_por_prod)
    idx_prod_max = unidades_por_prod.index(max_unidades)
    max_recaudacion = max(recaudacion_dias)
    idx_dia_max = recaudacion_dias.index(max_recaudacion)

    print(f"\n3. Destacados de la semana:")
    print(f"   - Producto más vendido:    {catalogo_productos[idx_prod_max]['nombre']} ({max_unidades} un.)")
    print(f"   - Día de mayor recaudación: {DIAS_SEMANA[idx_dia_max]} (${max_recaudacion:,.2f})")

    # 4. Productos sin ventas
    print("\n4. Productos sin ventas en toda la semana:")
    sin_ventas = [catalogo_productos[i]["nombre"] for i in range(6) if unidades_por_prod[i] == 0]
    if sin_ventas:
        for prod in sin_ventas:
            print(f"   - {prod}")
    else:
        print("   - Todos los productos registraron al menos una venta.")

    # 5. Total
    total_semana = sum(recaudacion_dias)
    print(f"\n5. RECAUDACIÓN TOTAL SEMANAL: ${total_semana:,.2f}")
    print("=============================================================\n")


# PROGRAMA PRINCIPAL


def main():
    ventas_matriz = cargar_ventas_desde_archivo()
    opcion = 0

    while opcion != 4:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
        except ValueError:
            print("\n[ERROR] Ingrese un número entero válido (1 a 4).\n")
            continue

        if opcion == 1:
            print("\n--- CATÁLOGO OFICIAL DE PRODUCTOS ---")
            for prod in catalogo_productos:
                print(f"  Cód. {prod['codigo']} | {prod['nombre']:<20} | ${prod['precio']:.2f}")
            print()

        elif opcion == 2:
            print("\n--- REGISTRO DE VENTA DIARIA ---")
            try:
                dia = int(input("Ingrese día (1=Lunes, 2=Martes, 3=Miércoles, 4=Jueves, 5=Viernes): "))
                if 1 <= dia <= 5:
                    cod = int(input("Ingrese código comercial del producto (101 a 106): "))
                    col = buscar_posicion_producto(cod)
                    if col != -1:
                        cant = int(input("Ingrese cantidad vendida: "))
                        if cant > 0:
                            ventas_matriz[dia - 1][col] += cant
                            subtotal = cant * catalogo_productos[col]["precio"]
                            print(f"\n[ÉXITO] Venta registrada: {catalogo_productos[col]['nombre']} x{cant}.")
                            print(f"Subtotal: ${subtotal:.2f}\n")
                        else:
                            print("\n[ERROR] La cantidad vendida debe ser mayor a 0.\n")
                    else:
                        print("\n[ERROR] El código comercial ingresado no existe en el catálogo.\n")
                else:
                    print("\n[ERROR] Día fuera de rango. Ingrese un entero del 1 al 5.\n")
            except ValueError:
                print("\n[ERROR] Entrada inválida. Ingrese datos numéricos.\n")

        elif opcion == 3:
            generar_informes_semanal(ventas_matriz)

        elif opcion == 4:
            guardar_ventas_en_archivo(ventas_matriz)
            print("¡Gracias por utilizar el sistema del Buffet!\n")

        else:
            print("\n[ERROR] Opción no válida. Elija un número de 1 a 4.\n")

if __name__ == "__main__":
    main()
