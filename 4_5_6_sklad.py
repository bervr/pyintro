# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
class Warehouse:
    total_storage_units_count = 30
    account_number_counter = 0


class Equipment(Warehouse):
    def __init__(self, model='noname', storage_units_per_one=1, eq_uid=0):
        if eq_uid == 0:
            Warehouse.account_number_counter += 1
            self.eq_uid = Warehouse.account_number_counter
        else:
            self.eq_uid = eq_uid
        self.eq_type = 'something'
        self.model = model
        self.storage_units_per_one = storage_units_per_one
        if Warehouse().total_storage_units_count > 0:
            Warehouse.total_storage_units_count -= self.storage_units_per_one
            # print(Warehouse().total_storage_units_count)
        else:
            print("Закончилось место на складе")
            del self


class Printer(Equipment):
    def __init__(self, model, storage_units_per_one=2, eq_uid=0):
        super().__init__(model, storage_units_per_one, eq_uid)
        self.eq_type = 'printer'


class Computer(Equipment):
    def __init__(self, model, storage_units_per_one=4, eq_uid=0):
        super().__init__(model, storage_units_per_one, eq_uid)
        self.eq_type = 'Computer'


class Phone(Equipment):
    def __init__(self, model, storage_units_per_one=1, eq_uid=0):
        super().__init__(model, storage_units_per_one, eq_uid)
        self.eq_type = 'IP phone'


noname_1 = Equipment()
printer_1 = Printer('hp3310', 1)
phone_1 = Phone('Cisco2950')
comp_1 = Computer('Dell')

print(Warehouse().total_storage_units_count)
print(printer_1.model, printer_1.eq_uid)
print(noname_1.model, noname_1.eq_uid)
print(comp_1.model, comp_1.eq_uid)
print(phone_1.model, phone_1.eq_uid)
