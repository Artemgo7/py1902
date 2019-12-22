import math  # импротируем модуль math

x = 3.265
# целое число, ближайшее целое снизу, ближайшее целое сверху
print(math.trunc(x), math.floor(x), math.ceil(x))

print(math.pi)  # константа пи
print(math.e)   # число Эйлера

y = math.sin(math.pi / 4)  # math.sin – синус
print(round(y, 2))

y = 1 / math.sqrt(2)  # math.sqrt – квадратный корень
print(round(y, 2))


#####################################
# логические операции

print('and:')
print(False and False) = FALSE
print(False and True) = FALSE
print(True and False) = FALSE
print(True and True) = TRUE
print()

print('or:')
print(False or False) = FALSE
print(False or True) = TRUE
print(True or False) = TRUE
print(True or True) = TRUE
print()

print('not:')
print(not False) = TRUE
print(not True) = FALSE
print()


# логические выражения

a = True
b = False
c = True
f = a and not b or c or (a and (b or c))
print(f)


#####################################
a = 2
b = 5

print(a < b)       # меньше
print(b > 3)       # больше
print(a <= 2)      # меньше или равно
print(b >= 7)      # больше или равно
print(a < 3 < b)   # двойное сравнение
print(a == b)      # равенство
print(a != b)      # неравенство
print(a is b)      # идентичность объектов в памяти
print(a is not b)  # a и b – разные объекты (хотя значения их могуть быть равны)


x = int(input('Enter the card: ')) #37000
r = int(x / 1000)
(r >= 37 and r <= 42) or (r >= 5500 and r <6000)
print()