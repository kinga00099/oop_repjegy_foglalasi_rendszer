class LegiTarsasag:
    def __init__(self, nev: str):
        self.nev = nev
        self.jaratok = []

    def __str__(self):
        return f"Légitársaság: {self.nev}"

    def jaratok_listazasa(self):
        if not self.jaratok:
            print("Nincs járat.")
        else:
            for jarat in self.jaratok:
                print(jarat)
