class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def gasto_por_folha(self):
        tabela = {
            "HB": 1,
            "2B": 2,
            "4B": 4,
            "6B": 6
        }
        return tabela[self.dureza]

    def __str__(self):
        return f"[{self.calibre}:{self.dureza}:{self.tamanho}]"


class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico = None
        self.tambor = []

    def insert(self, grafite: Grafite):
        if grafite.calibre != self.calibre:
            print("fail: calibre incompatível")
        return
        self.tambor.append(grafite)

    def pull(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
        return 
        if len(self.tambor) == 0:
            return  
        self.bico = self.tambor.pop(0)

    def remove(self):
        self.bico = None 

    def write(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        
        gasto = self.bico.gasto_por_folha()

        if self.bico.tamanho == 10:
            print("fail: tamanho insuficiente")
            return
        
        if self.bico.tamanho - gasto < 10:
            self.bico.tamanho = 10
            print("fail: folha incompleta")
            return

        self.bico.tamanho -= gasto

    def __str__(self):
        bico_str = str(self.bico) if self.bico is not None else "[]"
        tambor_str = "".join(str(g) for g in self.tambor)
        return f"calibre: {self.calibre}, bico: {bico_str}, tambor: <{tambor_str}>"
    

        



   