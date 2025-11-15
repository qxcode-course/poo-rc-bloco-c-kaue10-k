class Crianca:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade 

    def __str__ (self):
        return f"{self.nome},{self.idade}"
    
class Pulapula:
    def __int__(self):
        self.waiting = []
        self.playing = []

    def arrive(self, nome: str, idade: int):
        self.waiting.append(crianca(nome, idade))

    def enter(self):
        if not self.waiting:
