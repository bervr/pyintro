# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self._income.update({"wage": wage, "bonus": bonus})

    def get_full_name(self):
        print(f'Полное имя - {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии {sum(map(int, self._income.values()))}')


first_user = Position('Иван', 'Иванов', 'директор', 100, 50)
first_user.get_full_name()
first_user.get_total_income()
