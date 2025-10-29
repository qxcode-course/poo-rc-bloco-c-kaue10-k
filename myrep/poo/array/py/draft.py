class pessoa:

    


class onibus:
    def __init__(self, n_cadeiras: int):
        self.espera: list [pessoa] = []
        self.cadeiras: list[pessoa | None] = []
        for _ in range (n_cadeiras):
            self.cadeiras.append(None)

    def __str__(self):
        cadeiras = ",".join ([str (x) if x else "----" for x in self.cadeiras])
        espera = ",".join ([str(x) for x in self.espera])
        return f"cadeiras: [{self.cadeiras}\nespera:{self.espera}]"


david = pessoa("david")
print(david)
onibus = onibus(5)
onibus.espera.append(david)
onibus.espera.append(david)
onibus.espera.append(david)
onibus.espera.append(david)
onibus.espera.append(david)

