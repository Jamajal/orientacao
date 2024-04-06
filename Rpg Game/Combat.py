from abc import ABC, abstractmethod

class Combat(ABC):
    @abstractmethod
    def make_attack(self) -> int:
        pass

    @abstractmethod
    def take_damage(self) -> None:
        pass

    @abstractmethod
    def check_health(self) -> bool:
        pass

    @abstractmethod
    def die(self) -> bool:
        pass