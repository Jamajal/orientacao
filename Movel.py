from abc import ABC, abstractmethod

class Movel(ABC):
    @abstractmethod
    def pintar(self) -> None:
        pass
    
class Cadeira(Movel):
    def __init__(self, numero_de_pes: int, cor: str) -> None:
        super().__init__()
        self.numero_de_pes = numero_de_pes
        self.cor = cor
        
    def montar(self) -> None:
        pass
    
    def pintar(self, nova_cor: str) -> None:
        self.cor = nova_cor
    
if __name__ == '__main__':
    movel = Cadeira(cor='vermelha', numero_de_pes=3)
    
    print(movel.numero_de_pes)
    print(movel.cor)
    
    movel.pintar('azul')
    print(movel.cor)