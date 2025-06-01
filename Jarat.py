from abc import ABC


class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: int):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @property
    def jarat_tipus(self) -> str:
        return self._jarat_tipus

    @property
    def jegyar(self) -> int:
        return self._jegyar

    @jegyar.setter
    def jegyar(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("A jegyár csak pozitív egész szám lehet (Ft).")
        self._jegyar = value

    def __str__(self):
        return f"Típus: {self.jarat_tipus}, Járatszám: {self.jaratszam}, Célállomás: {self.celallomas}, Jegyár: {self.jegyar} Ft"


class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: int):
        super().__init__(jaratszam, celallomas, jegyar)
        self._jarat_tipus = "Belföldi"


class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: int):
        super().__init__(jaratszam, celallomas, jegyar)
        self._jarat_tipus = "Nemzetközi"
