from FoglalasiRendszer import FoglalasiRendszer
from Jarat import BelfoldiJarat, NemzetkoziJarat
from Legitarsasag import LegiTarsasag


def main():
    debreceni_jarat = BelfoldiJarat("B101", "Debrecen", 12000)
    londoni_jarat = NemzetkoziJarat("N201", "London", 45000)
    barcelonai_jarat = NemzetkoziJarat("N301", "Barcelona", 33000)

    ryanair = LegiTarsasag("Ryanair")
    wizzair = LegiTarsasag("Wizzair")

    ryanair.jaratok.append(debreceni_jarat)
    ryanair.jaratok.append(londoni_jarat)
    wizzair.jaratok.append(barcelonai_jarat)

    rendszer = FoglalasiRendszer([ryanair, wizzair])

    rendszer.foglalas_letrehozas(debreceni_jarat.jaratszam, "2025-07-01")
    rendszer.foglalas_letrehozas(debreceni_jarat.jaratszam, "2025-07-02")
    rendszer.foglalas_letrehozas(londoni_jarat.jaratszam, "2025-07-03")
    rendszer.foglalas_letrehozas(londoni_jarat.jaratszam, "2025-07-04")
    rendszer.foglalas_letrehozas(barcelonai_jarat.jaratszam, "2025-07-05")
    rendszer.foglalas_letrehozas(barcelonai_jarat.jaratszam, "2025-07-06")

    while True:
        print("\n--- Menü ---")
        print("1. Járatok listázása")
        print("2. Foglalások listázása")
        print("3. Jegy foglalása")
        print("4. Foglalás lemondása")
        valasz = input("Válassz egy lehetőséget (1-4): ")

        if valasz == "1":
            for tarsasag in [ryanair, wizzair]:
                print(f"\nLégitársaság: {tarsasag.nev}")
                tarsasag.jaratok_listazasa()

        elif valasz == "2":
            rendszer.foglalasok_listazasa()

        elif valasz == "3":
            jaratszam = input("Add meg a foglalni kívánt járatszámot: ")
            datum = input("Add meg a dátumot (formátum: YYYY-MM-DD): ")
            try:
                rendszer.foglalas_letrehozas(jaratszam, datum)
            except ValueError as e:
                print(e)

        elif valasz == "4":
            jaratszam = input("Add meg a törlendő foglalás járatszámát: ")
            datum = input("Add meg a dátumot (formátum: YYYY-MM-DD): ")
            try:
                rendszer.foglalas_lemondasa(jaratszam, datum)
            except ValueError as e:
                print(e)

        else:
            print("Érvénytelen választás.")


if __name__ == "__main__":
    main()
