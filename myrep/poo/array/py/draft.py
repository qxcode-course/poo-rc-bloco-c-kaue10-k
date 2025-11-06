class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return self.nome

class Onibus:
    def __init__(self, cadeiras: int):
        self.espera: list[Pessoa] = []
        self.cadeiras: list[Pessoa | None] = [None for _ in range(cadeiras)]

    def __str__(self):
        cadeiras_str = ", ".join([str(x) if x else "----" for x in self.cadeiras])
        espera_str = ", ".join([str(x) for x in self.espera])
        return f"Cadeiras: [{cadeiras_str}]\nEspera: [{espera_str}]"


david = Pessoa("david")
print(david)
onibus = Onibus(5)

onibus.espera.append(david)
onibus.espera.append(david)
onibus.espera.append(david)
onibus.espera.append(david)
onibus.espera.append(david)

print(onibus)

