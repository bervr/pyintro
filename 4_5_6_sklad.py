# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# # Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# # Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# # изученных на уроках по ООП.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    total_storage_units_count = 30
    account_number_counter = 0
    all_units = {}

    @staticmethod
    def check_storage():
        for el in Warehouse.all_units.keys():
            print(f'SCU № {el:05} содержится {Warehouse.all_units.get(el)}')

    @staticmethod
    def move_equipment(eq_type, dept):
        this_eq = Warehouse.all_units.get(Warehouse.get_one(eq_type))
        eq_unit = ''
        for el in ['eq_type', 'model']:
            eq_unit += f'{this_eq.get(el)} '
        eq_number = Warehouse.get_one(eq_type)
        Warehouse.all_units.update({eq_number: f"выдано в отдел {dept}"})
        print(f'Оборудование  № {eq_number :05} {eq_unit} выдано в отдел {dept}')
        Warehouse.total_storage_units_count += this_eq.get('storage SCU')

    def get_one(eq_type):
        for el in Warehouse.all_units.keys():
            if Warehouse.all_units.get(el).get('eq_type') == eq_type:
                return el


class Equipment(Warehouse, OwnError):
    def __init__(self, model='noname', storage_units_per_one=1, eq_uid=0):
        #print(str(eq_uid).isdigit(), str(storage_units_per_one).isdigit()  )
        try:
            if str(eq_uid).isdigit() and str(storage_units_per_one).isdigit():
                if eq_uid == 0:
                    Warehouse.account_number_counter += 1
                    self.eq_uid = Warehouse.account_number_counter
                else:
                    self.eq_uid = eq_uid
                self.eq_type = 'something'
                self.model = model
                self.storage_scu = storage_units_per_one
                print(f'создан {self.eq_uid:05} {self.eq_type} {self.model}')
            else:
                print(f'не могу создать обьект {eq_uid} {storage_units_per_one}')
                raise OwnError('какая-то беда с числами')

        except OwnError as err:
            print(err)
            del Equipment().self


    def save_storage(self):
        if self.eq_uid in list(Warehouse.all_units.keys()):
            Warehouse.total_storage_units_count += self.storage_scu
        if Warehouse().total_storage_units_count > self.storage_scu:
            Warehouse.total_storage_units_count -= self.storage_scu
            Warehouse.all_units.update({self.eq_uid: self.my_obj()})
            print(f'На склад принято оборудование {self.model} присвоен инвентарный номер {self.eq_uid:05}')
        else:
            print("Не достаточно места на складе для этого оборудования")
            del self


    def my_obj(self):
        return {'eq_type': self.eq_type, 'model': self.model, 'storage SCU': self.storage_scu}


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


my_noname_1 = Equipment()
my_noname_1.save_storage()
printer_1 = Printer('hp3310', 1)
printer_1.save_storage()
phone_1 = Phone('Cisco2950')
phone_1.save_storage()
comp_1 = Computer('Dell')
comp_1.save_storage()

comp_2 = Computer('Aquarius')
comp_2.save_storage()
comp_3 = Computer('HP')
comp_3.save_storage()

comp_4 = Computer('Sony', 'a', 333)
comp_4.save_storage()
comp_5 = Computer('fujimens', 3, 'b')
comp_5.save_storage()

print(comp_4.eq_uid, comp_5.eq_uid)




#print(comp_1.my_obj())
#print(f'{Warehouse.all_units} - весь склад')
print(f'{Warehouse().total_storage_units_count} осталось мест на складе')
# print(printer_1.model, printer_1.eq_uid)
# print(my_noname_1.model, my_noname_1.eq_uid)
# print(comp_1.model, comp_1.eq_uid)
# print(phone_1.model, phone_1.eq_type)
#Warehouse.check_storage()
Warehouse.move_equipment('Computer', "IT")
print(f'{Warehouse().total_storage_units_count} осталось мест на складе')
comp_2.save_storage()
print(f'{Warehouse().total_storage_units_count} осталось мест на складе')


print(f'{Warehouse().total_storage_units_count} осталось мест на складе')


print(f'{Warehouse.all_units} - весь склад')
