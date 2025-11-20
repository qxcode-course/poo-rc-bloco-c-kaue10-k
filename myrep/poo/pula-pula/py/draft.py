

class Crianca:
    def __init__(self, nome: str, idade: int, espera: str):
        self.nome = nome
        self.idade = idade 
        self.espera = espera

    def __str__(self):
        return f"{self.nome}:{self.idade}"


class Pulapula:
    def __init__(self):
        self.espera:list[Crianca] = []
        self.brincando:list[Crianca] = []

    def chegar(self, Crianca: Crianca):
        self.espera.append(Crianca)

    def entrar(self):
        if len(self.espera) == 0:
            return
    
    def sair(self):
        if len(self.brincando) == 0:
            return
        
        Crianca = self.brincando.pop()
        self.espera.insert(0, Crianca)

    def remover (self, nome: str):
        for i, Crianca in enumerate(self.brincando):
            if Crianca.nome == nome:
                self.brincando.pop(i)
                return
        
        print(f"fail: {nome} nao esta no pula-pula")

        def mostrar(self):

            espera_exibida = list(reversed(self.espera))

            bricando_exibido = list(reserved(self.brincando))

            print(f"[{','.join(map(str, espera_exibida))}] => [{','.join(map(str, brincando_exibido))}]
        




    def main():
        pula = Pulapula()

        while true:
            try:
                cmd = input(.strip().split)
                break
                

            if not cmd:
                continue 
                

            if cmd[0] == "fim":
                break
                
            if cmd[0] == "mostrar":
                pula.show()


            elif cmd[0] == "chegar":
                nome = cmd[1]
                idade = int(cmd[2])
                pula.chegar(nome, idade)

            elif cmd[0] == "entrar":
                pula.entrar()


            elif cmd [0] == "sair":
                pula.sair()
            
            elif cmd[0] == "remover":
                nome = cmd [1]
                pula.remover(nome)

    





    


