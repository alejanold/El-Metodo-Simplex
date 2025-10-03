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
