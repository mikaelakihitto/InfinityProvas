class Elevador:
    #metodo construtivo
    def __init__(self, totalCapacidade, atualCapacidade, totalAndar, atualAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = atualCapacidade
        self.totalAndar = totalAndar
        self.atualAndar = atualAndar
    
    def subir(self):
        if self.atualAndar == self.totalAndar:
            print('VOCE ESTA NO ANDAR MAIS ALTO')
        else:
            self.atualAndar+=1
            print('Subindo')
    
    def descer(self):
        if self.atualAndar == 0:
            print('VOCE JA ESTA NO TERREO')
        else:
            self.atualAndar+=1
            print('Subindo')

    def entrar(self):
        if self.atualCapacidade == self.totalCapacidade:
            print('O ELEVADOR ESTA CHEIO')
        else:
            self.atualCapacidade+=1
            print('Entrando uma pessoa')
    
    def sair(self):
        if self.atualCapacidade == 0:
            print('NAO TEM NINGUEM')
        else:
            self.atualCapacidade-=1
            print('Saindo uma pessoa')
    

infinityElevador = Elevador(10,0,3,0)

infinityElevador.descer()
infinityElevador.subir()
infinityElevador.subir()
infinityElevador.subir()
infinityElevador.subir()
infinityElevador.descer()

infinityElevador.sair()
for i in range(infinityElevador.totalCapacidade):
    infinityElevador.entrar()

infinityElevador.entrar()
