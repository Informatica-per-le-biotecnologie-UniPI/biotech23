# Data una stringa di DNA, ne ritornino il complemento.
from typing import Dict


def complementare(dna: str) -> str:
    """Complementa il dna dato.

    :param dna: Il dna da complementare.
    :return: Il dna complementato.
    """
    risultato = ""
    for nucleotide in dna:
        if nucleotide == "A":
            risultato += "T"
        elif nucleotide == "T":
            risultato += "A"
        elif nucleotide == "C":
            risultato += "G"
        elif nucleotide == "G":
            risultato += "C"
        else:
            raise ValueError(f"Atteso uno tra A, C, G, T, ma ho trovato un {nucleotide}")

    return risultato

def numero_mutazioni(dna: str) -> int:
    contatore_mutazioni = 0
    basi_ammesse = ["A", "C", "G", "T"]
    for base in dna:
        if base not in basi_ammesse:
            contatore_mutazioni += 1

    return contatore_mutazioni

# Data una stringa di DNA, ritorni la frequenza di ogni base canonica
def frequenza_basi(dna: str) -> dict:
    frequenze = {
        "A": 0,
        "T": 0,
        "C": 0,
        "G": 0,
    }
    for base in dna:
        if base in frequenze:
            frequenze[base] += 1

    return frequenze

# Data una stringa, ritorni la frequenza di ogni carattere.
def frequenza(sequenza: str) -> dict:
    frequenze = dict()
    for elemento in sequenza:
        if elemento not in frequenze:
            frequenze[elemento] = 0

        frequenze[elemento] += 1

    return frequenze


def frequenza_speciale(sequenza: str, caratteri_da_contare: list) -> dict:
    frequenze = dict()
    for elemento in sequenza:
        if elemento in caratteri_da_contare:
            if elemento not in frequenze:
                frequenze[elemento] = 0

            frequenze[elemento] += 1

    return frequenze


# Date due stringhe di DNA di uguale lunghezza, conti il numero di caratteri diversi.
def mismatch(dna_a: str, dna_b: str) -> int:
    mismatch_counter = 0
    for posizione, (base_a, base_b) in enumerate(zip(dna_a, dna_b)):
        if base_a != base_b:
            mismatch_counter += 1

    return mismatch_counter

print(mismatch("ACT", "ATC"))
# print(frequenza_speciale("ACGTHBBBBBB", ["A", "B", "H"]))
