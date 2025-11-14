class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def gasto(self):
        tabela = {
            "HB":1,
            "2B":2,
            "4B":4,
            "6B":6,
        }

        return tabela.get(self.dureza, 0)
    
    def __str__(self):
        return f"{self.calibre}:{self.dureza}:{self.tamanho}"

class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico = None
        self.tambor = []
    

    def insert (self.calibre: float):




        



   