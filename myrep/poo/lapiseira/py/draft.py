class grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

def __str__(self):
    return f"{self.calibre}mm,{self.dureza}m{self.tamanho}mm" 

class lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico = None
        self.tambor = []

    def __str__(self):
        bico_str = str(self.bico) if self.bico else "vazio"
        return f""
