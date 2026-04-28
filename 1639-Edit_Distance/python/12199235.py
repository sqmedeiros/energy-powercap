def edit_distance(s1, s2):
    n = len(s1)
    m = len(s2)

    # Siempre hacemos que s1 sea la cadena más corta
    if n > m:
        s1, s2 = s2, s1
        n, m = m, n

    # Usamos una sola fila para la distancia de edición
    prev = list(range(m + 1))

    # El ciclo principal de la DP
    for i in range(1, n + 1):
        curr = [i] * (m + 1)  # Inicializamos la fila actual
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1]  # No se necesita operación si los caracteres coinciden
            else:
                # Escogemos la operación más eficiente (reemplazar, agregar, eliminar)
                curr[j] = min(prev[j - 1] + 1,  # Reemplazar
                              prev[j] + 1,      # Eliminar
                              curr[j - 1] + 1)  # Agregar
        prev = curr  # Guardamos la fila actual como la fila anterior para la siguiente iteración

    return prev[m]

# Entrada
s1 = input().strip()
s2 = input().strip()

# Salida
print(edit_distance(s1, s2))