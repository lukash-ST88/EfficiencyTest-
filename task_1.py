# более наглядный пример
def isEven(value):
    return value % 2 == 0


# менее читабельный пример использующий побитовое сравнение с логическим И
# более быстрая функция
def my_is_even(value):
    return not value & 1
