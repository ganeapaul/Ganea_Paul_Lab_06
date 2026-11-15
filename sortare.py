
from pathlib import Path

FISIER = Path(__file__).with_name("date.txt")


def insertion_sort(numere):
    rezultat = numere.copy()

    for i in range(1, len(rezultat)):
        valoare = rezultat[i]
        j = i - 1

        while j >= 0 and rezultat[j] > valoare:
            rezultat[j + 1] = rezultat[j]
            j -= 1

        rezultat[j + 1] = valoare

    return rezultat


def merge_sort(numere):
    if len(numere) <= 1:
        return numere.copy()

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


def citeste_date(cale):
    try:
        with open(cale, "r", encoding="utf-8") as fisier:
            linie_numere = fisier.readline()
            linie_algoritm = fisier.readline()
    except FileNotFoundError:
        print("Eroare: fisierul date.txt nu exista.")
        return None
    except OSError as eroare:
        print(f"Eroare la citirea fisierului: {eroare}")
        return None

    if not linie_numere.strip() or not linie_algoritm.strip():
        print("Eroare: primele doua linii trebuie sa contina numere si algoritmul ales.")
        return None

    try:
        numere = [int(cifra) for cifra in linie_numere.split()]
    except ValueError:
        print("Eroare: prima linie trebuie sa contina doar numere intregi separate prin spatii.")
        return None

    alegere = linie_algoritm.strip().lower()

    if alegere not in ("insertion", "merge"):
        print("Eroare: algoritmul trebuie sa fie Insertion sau Merge.")
        return None

    return numere, alegere


def adauga_rezultat(cale, algoritm, numere_sortate):
    with open(cale, "rb") as fisier:
        fisier.seek(0, 2)
        marime = fisier.tell()

        if marime > 0:
            fisier.seek(-1, 2)
            are_linie_noua = fisier.read(1) == b"\n"
        else:
            are_linie_noua = True

    with open(cale, "a", encoding="utf-8") as fisier:
        if not are_linie_noua:
            fisier.write("\n")

        sir_numere = " ".join(str(nr) for nr in numere_sortate)
        fisier.write(f"{algoritm}: {sir_numere}\n")


def main():
    date = citeste_date(FISIER)

    if date is None:
        return

    numere, alegere = date

    if alegere == "insertion":
        rezultat = insertion_sort(numere)
        nume_algoritm = "Insertion"
    else:
        rezultat = merge_sort(numere)
        nume_algoritm = "Merge"

    try:
        adauga_rezultat(FISIER, nume_algoritm, rezultat)
    except OSError as eroare:
        print(f"Eroare la scrierea in fisier: {eroare}")
        return

    print(f"{nume_algoritm}: {' '.join(str(nr) for nr in rezultat)}")
    print("Rezultatul a fost adaugat in date.txt.")


if __name__ == "__main__":
    main()
