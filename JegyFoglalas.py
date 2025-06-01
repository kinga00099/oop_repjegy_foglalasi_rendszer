from datetime import datetime, date

from Jarat import Jarat


class JegyFoglalas:
    def __init__(self, jarat: Jarat, datum: str):
        self.jarat = jarat
        self.datum = datum

    @property
    def datum(self):
        return self._datum

    @datum.setter
    def datum(self, datum: str):
        try:
            datum_obj = datetime.strptime(datum, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("A dátum formátuma helytelen. (Helyes: ÉÉÉÉ-HH-NN)")
        if datum_obj < date.today():
            raise ValueError("A foglalás dátuma nem lehet múltbeli.")
        self._datum = datum_obj

    def __str__(self):
        return f"Típus: {self.jarat.jarat_tipus}, Járat: {self.jarat.jaratszam}, Cél: {self.jarat.celallomas}, Dátum: {self.datum}, Jegyár: {self.jarat.jegyar} Ft"
