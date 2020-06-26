# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) —
# 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
import time
from termcolor import colored, cprint
import colorama
colorama.init()

class TrafficLight:
    color = 'yellow'
    def __running(self):
        def print_light(x, wait_time):
            cprint(f'цвет {x}, секунд - {wait_time}', x, end='')
            time.sleep(wait_time)
            print('\r', end='')
        while True:
            self.color = 'red'
            print_light(self.color, 7)
            self.color = 'yellow'
            print_light(self.color, 2)
            self.color = 'green'
            print_light(self.color, 7)


traffic_light = TrafficLight()
traffic_light._TrafficLight__running()
