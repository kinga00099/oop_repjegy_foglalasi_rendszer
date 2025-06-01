from datetime import datetime, date

from JegyFoglalas import JegyFoglalas


class FoglalasiRendszer:
    def __init__(self, legitarsasagok: list):
        self.foglalasok = []
        self.legitarsasagok = legitarsasagok

    def foglalas_letrehozas(self, jaratszam: str, datum: str):
        jarat = self.jarat_kereses(jaratszam)
        if not jarat:
            raise ValueError("Nincs ilyen járat.")
        foglalas = JegyFoglalas(jarat, datum)
        self.foglalasok.append(foglalas)
        print(f"Foglalás sikeres:\n{foglalas}")

    def foglalas_lemondasa(self, jaratszam: str, datum: str):
        jarat = self.jarat_kereses(jaratszam)
        if not jarat:
            raise ValueError("Nincs ilyen járat.")

        try:
            datum_obj = datetime.strptime(datum, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("A dátum formátuma helytelen. (Helyes: ÉÉÉÉ-HH-NN)")

        if datum_obj < date.today():
            raise ValueError("Múltbeli foglalás nem törölhető.")

        lemondando = None
        for foglalas in self.foglalasok:
            if foglalas.jarat.jaratszam == jaratszam and foglalas.datum == datum_obj:
                lemondando = foglalas
                break

        if lemondando:
            self.foglalasok.remove(lemondando)
            print("A foglalás sikeresen törölve lett.")
        else:
            print("Nincs ilyen foglalás.")

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincsenek foglalások.")
        else:
            for foglalas in self.foglalasok:
                print(foglalas)

    def jarat_kereses(self, jaratszam: str):
        for tarsasag in self.legitarsasagok:
            jarat = next((jarat for jarat in tarsasag.jaratok if jarat.jaratszam == jaratszam), None)
            if jarat:
                return jarat
        return None
