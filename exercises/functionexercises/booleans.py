def all_(elements: list) -> bool:
    """Verifica che tutte le espressioni siano vere.

    :param elements: Lista di espressioni booleane.
    :return: True se tutte le espressioni valutano a True, e False altrimenti.
    """
    # lista vuota
    #

    # lista con diversi elementi
    valutazione_parziale = elements[0]
    if not valutazione_parziale:
        # non serve un else perche' il return termina la funzione
        return False

    for index, elemento_corrente in enumerate(elements[1:]):
        if not elemento_corrente:
            print(f"Trovato elemento falso in posizione {index + 1}")
            # l'elemento corrente e' falso
            return False

    # ho scorso tutta la lista, e non ho trovato elementi falsi
    return True

def any_(elements: list) -> bool:
    """C'e' almeno un elemento vero in elements?

    :param elements: Lista di espressioni booleane
    :return: True se c'e' almeno una espressione vera, False altrimenti.
    """
    # cerco il primo elemento True
    return index_(elements, True)


# print(all_([]))
# print(all_([True]))
# print(all_([False]))
# print(all_([False or True]))
# print(all_([True, False, False, True, False]))
# print(all_([True, True]))
