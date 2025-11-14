import sys

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
        if not self.espera:
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

        self.caixas[indice] = None


def main():
    mercantil = None  
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        print(f"${line}")
        ui = line.split()
        cmd = ui[0]

        try:
            if cmd == "end":
                break

            elif cmd == "init":
                qtd = int(ui[1])
                mercantil = Mercantil(qtd)

            elif cmd == "show":
                if mercantil is None:
                    print("fail: mercantil não inicializado")
                else:
                    print(mercantil)

            elif cmd == "arrive":
                if mercantil is None:
                    print("fail: mercantil não inicializado")
                else:
                    mercantil.chegar(Cliente(ui[1]))

            elif cmd == "call":
                if mercantil is None:
                    print("fail: mercantil não inicializado")
                else:
                    mercantil.chamar(int(ui[1]))

            elif cmd == "finish":
                if mercantil is None:
                    print("fail: mercantil não inicializado")
                else:
                    mercantil.finalizar(int(ui[1]))

            else:
                print("fail: comando invalido")

        except IndexError:
            print(f"fail: argumentos insuficientes para {cmd}")
        except ValueError:
            print(f"fail: argumento inválido para {cmd}")
        except Exception as e:
            print(f"fail: erro ao executar {cmd}: {e}")


if __name__ == "__main__":
    main()

