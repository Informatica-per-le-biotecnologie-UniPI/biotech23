def index_(elements: list, searching_for):
    """Restituisce la posizione dell'elemento searching_for in elements, se presente, altrimenti None.

    :param elements: Collezione in cui vogliamo trovare l'elemento.
    :param searching_for: L'elemento che stiamo cercando.
    :return: L'indice dell'elemento se presente, None altrimenti.
    """
    # itero sugli elementi
    for (i, elemento_corrente) in enumerate(elements):
        # elemento corrente: confronto elemento con searching_for
        if elemento_corrente == searching_for:
            # ritorno l'indice
            return i


    # ho finito di scorrere la lista
    # ritorno None
    return None


def subtract_list(a_list, another_list) -> set:
    """Crea un set con tutti gli elementi in a_list che non sono in another_list.

    :param a_list: Una lista
    :param another_list: La lista sottraente
    :return: Tutti gli elementi che sono in a_list, ma non in another_list
    """
    # se another_list e' vuota, ritorno a_list
    if len(another_list) == 0 or len(a_list) == 0:
    # MOLTO SBAGLIATO! len(another_list) or len(a_list) == 0
        return a_list

    # se sono uguali niente
    if a_list == another_list:
        return []

    # confronto ogni elemento di a_list con un elemento di another_list
    # itero su a_list
        # elemento corrente e' in another_list
        # true
        #
        # false
        # niente

    # ritorno a_list

subtract_list([0, 1, 2] [2, 3, 4]) # [0, 1]
subtract_list([], [1, 2, 3]) # []
subtract_list([1, 2], [1, 2, 3]) # []




# print(index_(elements=[], searching_for="ACT") == None)
# print(index_([1], 3) == None)
# print(index_([1, 2, 3], 1) == 0)
# print(index_([1, 2, 3], 2) == 1)
# print(index_([1, 2, 3], 3) == 2)
# index_([1, 2], 2)










