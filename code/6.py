a = input("Введите последовательность чисел разделенных пробелом: ")

my_list = list(map(int, a.split()))
my_tuple = tuple(my_list)

print(f"Список: {my_list}")
print(f"Кортеж: {my_tuple}")