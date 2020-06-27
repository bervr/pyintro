# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')

    def show_speed(self):
        print(f'Текущая вкорость {self.name} - {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self, speed):
        self.speed = speed
        if self.speed < 60:
            print(f'Текущая вкорость {self.name} - {self.speed} км/ч')
        else:
            print(f'{self.name}! Превышение на {60 - self.speed} км/ч!')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self, speed):
        self.speed = speed
        if self.speed < 40:
            print(f'Текущая вкорость {self.name} - {self.speed} км/ч')
        else:
            print(f'{self.name}! Превышение на {40 - self.speed} км/ч!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

police_203 = PoliceCar(90, 'black with white line' , 'NYPD 203')
work_1 = WorkCar(30, 'strange, maybe was red' , 'Kamaz')
sport_1 = SportCar(450, 'blue', 'F1 McLauren')
town_1 = TownCar (50, 'metalyc white', 'lasto4ka')

police_203.show_speed()
work_1.show_speed(41)
sport_1.show_speed()
town_1.show_speed(70)
sport_1.turn("направо")
police_203.turn('за ней')
town_1.stop()
work_1.show_speed(39)
work_1.turn('налево')
town_1.go()