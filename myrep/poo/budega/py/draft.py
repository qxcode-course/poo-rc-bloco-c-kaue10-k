class cliente: 
    
    def __init__(self, nome: str):
        self.nome = nome
    
    def getNome(self) -> str:
        return self.__nome
    
    def __str__(self) -> str:
        return self.__nome
    
class market:
    
    def__init__(self, qtd_caixas: int):
    self.caixas = [none for _ in range (qtd_caixas)]
    self.espera = []
