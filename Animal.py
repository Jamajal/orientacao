class Animal:
    def __init__(self, numero_de_patas: int) -> None:
        self.numero_de_patas = numero_de_patas
        
    def fazer_barulho(self) -> None:
        print("Eu sou um animal")
        
class Cachorro(Animal):
    def __init__(self, numero_de_patas: int, cor: str) -> None:
        super().__init__(numero_de_patas)
        self.__cor = cor
        
    def fazer_barulho(self) -> None:
        print("AU AU !!!!")
        

    

    