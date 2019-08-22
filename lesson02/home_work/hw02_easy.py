# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
i = 1
for itm in fruits:
    print('{}. {:>7}'.format(i, itm))
    i = i+1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_2 = [1, 2, 4, 5, 6, 8]

for itm in lst_2:
    if itm in lst_1:
        lst_1.remove(itm)
print(lst_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

lst_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_4 = []

for itm in lst_3:
    if itm % 2 == 0:
        lst_4.append(itm/4)
    else:
        lst_4.append(itm*2)

print(lst_4)
