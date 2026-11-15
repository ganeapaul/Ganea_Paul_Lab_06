import re
from pathlib import Path

FISIER = Path(__file__).with_name("date.txt")

def insertion_sort(numere):
    for i in range(1, len(numere)):
        valoare = numere[i]
        j = i - 1

        while j >= 0 and numere[j] > valoare:
            numere[j + 1] = numere[j]
            j -= 1

        numere[j + 1] = valoare

    return numere

def merge_sort(numere):
    if len(numere) <= 1:
        return numere

    mijloc = len(numere) // 2

    stanga = merge_sort(numere[:mijloc])
    dreapta = merge_sort(numere[mijloc:])

    rezultat = []
    i = 0
    j = 0

    while i < len(stanga) and j < len(dreapta):
        if stanga[i] <= dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1

    rezultat.extend(stanga[i:])
    rezultat.extend(dreapta[j:])

    return rezultat



def citeste_date():
    try:
        with open(FISIER, "r", encoding="utf-8") as f:
            linia1 = f.readline()
            linia2 = f.readline()

    except FileNotFoundError:
        print("Eroare: fisierul date.txt nu exista!")
        return None

    except OSError as eroare:
        print("Eroare la citire:", eroare)
        return None

    if not linia1.strip() or not linia2.strip():
        print("Eroare: fisierul trebuie sa contina doua linii valide!")
        return None

    # Verificam fiecare numar inainte de conversie
    elemente = linia1.split()

    for x in elemente:
        if not re.fullmatch(r"[+-]?[0-9]+", x):
            print("Eroare: numar invalid!", x)
            return None

    numere = [int(x) for x in elemente]

    # Verificam algoritmul
    algoritm = linia2.strip().lower()

    if algoritm not in ("insertion", "merge"):
        print("Eroare: algoritmul trebuie sa fie Insertion sau Merge!")
        return None

    return numere, algoritm


def scrie_rezultat(algoritm, rezultat):
    try:
        with open(FISIER, "rb") as f:
            continut = f.read()

        separator = ""
        if continut and not continut.endswith((b"\n", b"\r")):
            separator = "\n"

        with open(FISIER, "a", encoding="utf-8") as f:
            f.write(separator)
            f.write(algoritm + ": ")
            f.write(" ".join(str(x) for x in rezultat))
            f.write("\n")

    except OSError as eroare:
        print("Eroare la scrierea fisierului:", eroare)
        return False

    return True


def main():
    date = citeste_date()

    if date is None:
        return

    numere, algoritm = date

    if algoritm == "insertion":
        rezultat = insertion_sort(numere)
        nume = "Insertion"
    else:
        rezultat = merge_sort(numere)
        nume = "Merge"

    if scrie_rezultat(nume, rezultat):
        print("Algoritm utilizat:", nume)
        print("Numere sortate:", rezultat)
        print("Rezultatul a fost salvat in date.txt")


if __name__ == "__main__":
    main()
