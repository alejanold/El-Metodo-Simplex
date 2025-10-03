def imprimir_tabla(tabla, variables, basicas):
  print("\nTabla actual:")
  encabezado = "     "
  for nombre in variables:
    encabezado += f"{nombre:^10}"
    print(encabezado)

for i, fila in enumerate(tabla):
  if i == 0:
            nombre = "Z"
        else:
            nombre = basicas[i - 1]
        fila_str = f"{nombre:<4}"
        for valor in fila:
            fila_str += f"{valor:10.2f}"
        print(fila_str)
    print("-" * 50)

def simplex(coef_objetivo, restricciones, lados_derechos, maximizar=True):
    num_restricciones = len(restricciones)
    num_variables = len(coef_objetivo)

# Para hacer la tabla inicial
    filas = num_restricciones + 1
    columnas = num_variables + num_restricciones + 1
    tabla = [[0.0 for _ in range(columnas)] for _ in range(filas)]

# Fila Z
    for j in range(num_variables):
        if maximizar:
            tabla[0][j] = -coef_objetivo[j]
        else:
            tabla[0][j] = coef_objetivo[j]

# Para las Restricciones y las holguras
    for i in range(num_restricciones):
        for j in range(num_variables):
            tabla[i + 1][j] = restricciones[i][j]
        tabla[i + 1][num_variables + i] = 1 
        tabla[i + 1][-1] = lados_derechos[i]

# Para crear nombres en las variables
    variables = []
    for i in range(num_variables):
        variables.append(f"x{i+1}")
    for i in range(num_restricciones):
        variables.append(f"s{i+1}")
    variables.append("RHS")

    basicas = [f"s{i+1}" for i in range(num_restricciones)]

    imprimir_tabla(tabla, variables, basicas)

iteracion = 1
    while True:
        # Aqui comienzo a buscar la  columna pivote (o en dado caso el no. más negativo en fila Z)
        col_pivote = -1
        minimo = 0
        for j in range(columnas - 1):
            if tabla[0][j] < minimo:
                minimo = tabla[0][j]
                col_pivote = j
        if col_pivote == -1:
            print("No hay más coeficientes negativos en Z. ¡Solución óptima encontrada!")
            break

      # Continuo buscando la fila pivote (o la de menor razón positiva)
        fila_pivote = -1
        menor_razon = float("inf")
        for i in range(1, filas):
            if tabla[i][col_pivote] > 0:
                razon = tabla[i][-1] / tabla[i][col_pivote]
                if razon < menor_razon:
                    menor_razon = razon
                    fila_pivote = i
        if fila_pivote == -1:
            print("Problema ilimitado.")
            return
        print(f"\nIteración {iteracion}: Columna pivote = {col_pivote+1}, Fila pivote = {fila_pivote+1}")

