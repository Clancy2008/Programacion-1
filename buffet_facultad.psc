Algoritmo BuffetFacultad
	
	Dimension nombres[6]
	Dimension precios[6]
	Dimension ventas[5,6] // 5 días (filas) x 6 productos (columnas)
	
	
	nombres[1] <- "Café con leche"
	precios[1] <- 1500
	
	nombres[2] <- "Medialuna"
	precios[2] <- 700
	
	nombres[3] <- "Sándwich de miga"
	precios[3] <- 1800
	
	nombres[4] <- "Agua mineral"
	precios[4] <- 1000
	
	nombres[5] <- "Empanada"
	precios[5] <- 1200
	
	nombres[6] <- "Chipá"
	precios[6] <- 1300
	
	
	Para f <- 1 Hasta 5 Con Paso 1 Hacer
		Para c <- 1 Hasta 6 Con Paso 1 Hacer
			ventas[f,c] <- 0
		FinPara
	FinPara
	
	opcion <- 0
	
	
	Mientras opcion <> 4 Hacer
		Escribir "================================="
		Escribir "      BUFFET DE LA FACULTAD      "
		Escribir "================================="
		Escribir "1. Ver Catálogo de Productos"
		Escribir "2. Registrar Venta"
		Escribir "3. Ver Informe de Recaudación"
		Escribir "4. Salir"
		Escribir "Elija una opción (1-4): "
		Leer opcion
		
		Segun opcion Hacer
			1:
				Escribir "--- CATÁLOGO DE PRODUCTOS ---"
				Para i <- 1 Hasta 6 Con Paso 1 Hacer
					Escribir i, ". ", nombres[i], " - $", precios[i]
				FinPara
				
			2:
				Escribir "--- REGISTRAR VENTA ---"
				Escribir "Ingrese día (1=Lunes, 2=Martes, 3=Miércoles, 4=Jueves, 5=Viernes): "
				Leer dia
				
				Si dia >= 1 Y dia <= 5 Entonces
					Escribir "Ingrese número de producto (1 al 6): "
					Leer prod
					
					Si prod >= 1 Y prod <= 6 Entonces
						Escribir "Ingrese cantidad vendida: "
						Leer cant
						
						Si cant > 0 Entonces
							// Acumular la cantidad en la matriz
							ventas[dia, prod] <- ventas[dia, prod] + cant
							subtotal <- cant * precios[prod]
							Escribir "[ÉXITO] Venta registrada. Subtotal: $", subtotal
						Sino
							Escribir "[ERROR] La cantidad debe ser mayor a 0."
						FinSi
					Sino
						Escribir "[ERROR] Producto no válido (debe ser del 1 al 6)."
					FinSi
				Sino
					Escribir "[ERROR] Día no válido (debe ser del 1 al 5)."
				FinSi
				
			3:
				Escribir "--- INFORME DE RECAUDACIÓN SEMANAL ---"
				totalGeneral <- 0
				Para f <- 1 Hasta 5 Con Paso 1 Hacer
					totalDia <- 0
					Para c <- 1 Hasta 6 Con Paso 1 Hacer
						totalDia <- totalDia + (ventas[f,c] * precios[c])
					FinPara
					Escribir "Día ", f, ": $", totalDia
					totalGeneral <- totalGeneral + totalDia
				FinPara
				Escribir "---------------------------------"
				Escribir "TOTAL GENERAL SEMANAL: $", totalGeneral
				
			4:
				Escribir "¡Gracias por utilizar el sistema del Buffet!"
				
			De Otro Modo:
				Escribir "[ERROR] Opción inválida. Intente de nuevo."
		FinSegun
		
		Escribir ""
	FinMientras
FinAlgoritmo
