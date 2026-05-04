# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    answer = []
    for list in matrix:
        for elemento in list:
            answer.append(elemento)
    return answer


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    answer = []
    for fila in matrix:
        suma = sum(fila)
        answer.append(suma)
    return answer


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    if not matrix:
        return []

    answer = []
    cant_columnas = len(matrix[0])
    for columna in range(cant_columnas):
        suma_columna = 0
        for fila in matrix:
            suma_columna += fila[columna]
        answer.append(suma_columna)
    return answer
