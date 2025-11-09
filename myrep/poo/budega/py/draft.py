class Cliente:
    def __init__(self, nome: str):
        self.__nome = nome

    def get_nome(self) -> str:
        return self.__nome

    def __str__(self) -> str:
        return self.__nome


class Mercantil:
    def __init__(self, qtd_caixas: int):
    
        self.caixas: list[Cliente | None] = [None for _ in range(qtd_caixas)]
        
        self.espera: list[Cliente] = []

    def __str__(self) -> str:
        caixas_str = ", ".join(str(c) if c is not None else "-----" for c in self.caixas)
        fila_str = ", ".join(str(p) for p in self.espera)
        return f"Caixas: [{caixas_str}]\nEspera: [{fila_str}]"

    def chegar(self, cliente: Cliente):
        self.espera.append(cliente)

    def chamar(self, indice: int):
        if indice < 0 or indice >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if self.caixas[indice] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return
        
        cliente = self.espera.pop(0)
        self.caixas[indice] = cliente

        def finalizar(self, indice: int):
            if indice < 0 or indice >= len(self.caixas):
                print("fail: caixa inexistente")
            return
            if self.caixas[indice] is None:
                print("fail: caixa vazio")
            return

        cliente = self.caixas[indice]
        self.caixas[indice] = None
        return cliente