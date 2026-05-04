# Replace the "ANSWER HERE" for your answer

def enumerate_list(lst):
    """
    Dada una lista de strings, retorna una nueva lista donde cada elemento
    tiene el formato "indice. valor". Los strings vacios se deben saltear
    y no deben aparecer en la lista resultante.
    El indice debe ser consecutivo (no el indice original).

    Ejemplo: enumerate_list(["Red", "Green", "", "White"]) -> ["0. Red", "1. Green", "2. White"]
    """
    list = []
    i = 0
    for elemento in lst:
        if elemento != "":
            list.append(f"{i}. {elemento}")
            i = i + 1
    return list


def enumerate_backwards(lst):
    """
    Igual que enumerate_list, pero cada palabra debe estar escrita al reves.
    Los strings vacios se deben saltear.

    Ejemplo: enumerate_backwards(["Red", "Green", ""]) -> ["0. deR", "1. neerG"]
    """
    list = []
    i = 0
    for elemento in lst:
        if elemento != "":
            backwards = ""
            for letras in elemento:
                backwards = letras + backwards
            list.append(f"{i}. {backwards}")
            i = i + 1
    return list
