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
