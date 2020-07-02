# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @prop
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calculate_textile(self):
        pass


class Suite(Clothes):
    def calculate_textile(self):
        return round(self.size * 2 + 0.3)


class Coat(Clothes):
    @property
    def calculate_textile(self):
        return round(self.size / 6.5 + 0.5)


suite_1 = Suite(56)
coat_1 = Coat(190)
print(suite_1.calculate_textile())
print(coat_1.calculate_textile)
