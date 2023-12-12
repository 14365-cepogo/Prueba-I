def es_tablero_valido(tablero):
    """
    Verifica si un tablero de 8 reinas es válido.

    Args:
    - tablero: Una lista de 8 enteros, donde cada elemento representa la columna
               en la que se encuentra la reina en la fila correspondiente.

    Returns:
    - True si el tablero es válido, False de lo contrario.
    """
    for i in range(8):
        for j in range(i + 1, 8):
            # Verifica si hay dos reinas en la misma columna
            if tablero[i] == tablero[j]:
                return False

            # Verifica si hay dos reinas en la misma diagonal
            if abs(tablero[i] - tablero[j]) == abs(i - j):
                return False

    # Si no se encontraron problemas, el tablero es válido
    return True

def imprimir_tablero(tablero):
    """
    Imprime un tablero de 8 reinas.

    Args:
    - tablero: Una lista de 8 enteros, donde cada elemento representa la columna
               en la que se encuentra la reina en la fila correspondiente.
    """
    for fila in range(8):
        fila_str = ""
        for columna in range(8):
            if tablero[fila] == columna:
                fila_str += " Q "
            else:
                fila_str += " . "
        print(fila_str)

# Ejemplo de uso
tablero_ejemplo = [4, 0, 7, 5, 2, 6, 1, 3]

if es_tablero_valido(tablero_ejemplo):
    print("El tablero es válido:")
    imprimir_tablero(tablero_ejemplo)
else:
    print("El tablero no es válido.")
