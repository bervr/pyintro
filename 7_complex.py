# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата
class ComplexClass:
    def __init__(self, complex):
        self.my_complex = complex
        # print(self.my_complex)

    def __add__(self, other):
        return complex((self.my_complex.real + other.my_complex.real), (self.my_complex.imag + other.my_complex.imag))

    def __mul__(self, other):
        return complex((self.my_complex.real * other.my_complex.real - self.my_complex.imag * other.my_complex.imag),
                       (self.my_complex.real * other.my_complex.real + self.my_complex.imag * other.my_complex.imag))


complex_1 = ComplexClass(2 + 3j)
complex_2 = ComplexClass(5 + 0j)
print(f'Сумма комплексных чисел равна {complex_1 + complex_2}')
print(f'Произведение комплексных чисел равно {complex_1 * complex_2}')
