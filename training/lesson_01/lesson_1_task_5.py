# Создаем функцию, которая принимает параметр num и печатает его
def print_digit(num):
    # end="" нужно, чтобы цифры печатались в одну сроку. а не столбиком
    print(num, end="")


# Вызываем функцию 11 раз вручную, передавая каждую цифру номера
print_digit(8)
print_digit(8)
print_digit(0)
print_digit(0)
print_digit(5)
print_digit(5)
print_digit(5)
print_digit(3)
print_digit(5)
print_digit(3)
print_digit(5)

# Пустой print в конце для перевода строки (чтобы следующая команда терминала
# не прилипала к номеру телефона)
print()
