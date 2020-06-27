# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и
# проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    handle_count = 0

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запук отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Ручка  пишет')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш чертит')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        Stationery.handle_count += 1

    def draw(self):
        if Stationery.handle_count <= 1:
            print('Имея всего один маркер можно разривовать все что угодно, кроме этого маркера')
        else:
            print('Имея 2 маркера - можно разрисовать все что угодно!')


clip = Stationery('скрепка')
clip.draw()
pen = Pen('ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('черный маркер')
handle.draw()
handle2 = Handle('красный маркер')
handle2.draw()
print(handle.title)
print(handle2.title)
