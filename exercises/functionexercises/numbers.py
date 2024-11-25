def min_(elements: list):
    """Calcola il minimo di elements.

    :param elements: Collezione di oggetti.
    :return: Il minimo di elements.
    """
    # lista vuota
    if len(elements) == 0:
        return None

    # lista non vuota
    # lista con un elemento
    if len(elements) == 1:
        # modifico valore: side-effect
        # elements[0] = None
        # riassegno: non ho side-effect!
        elements = [1, 2, 5]
        # restituisco l'elemento
        return elements[0]  # si conta da 0!

    # lista con piu' elementi
    # minimo corrente e' il primo elemento
    minimo_corrente = elements[0]
    # itero
    for elemento_corrente in elements[1:]:
        print(f"Confronto {minimo_corrente} con {elemento_corrente}")
        # confronto l'elemento corrente con minimo corrente
        # se e' minore...
        if elemento_corrente <= minimo_corrente:
            # allora aggiorno minimo corrente
            minimo_corrente = elemento_corrente
            print(f"    il nuovo minimo_corrente e' {minimo_corrente}")
        # se l'elemento e' maggiore, allora non devo aggiornare

    return minimo_corrente

print(help(min_))


# print(min_([]))
# print(min_([5]))
# print(min_([3]))
print(min_([0, 1, 2]))
# print(min_([2, 1, 0]))
# print(min_([0, +1, -1]))

# if min_([]) == None and min_([0, 1, -10]) == -10 and min_([0, 0, 0]) == 0:
#     print("min_ funziona")
# else:
#     print("min_ non funziona")

