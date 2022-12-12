from random import randint

'''Сортировка методом пузырька'''

length = randint(5, 20)  # длина массива
arr = [randint(1, 1000) for num in range(length)]  # генератор рандомных чисел

print(f'1) Не отсортированный массив : {arr}')

print('#^#' * 30)
for i in range(length - 1):
    for j in range(length - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # print(arr) - вывод сортировки по шагам

print(f'2) Отсортированный массив : {arr}')

for i in range(length - 1):
    for j in range(length - i - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # print(arr) - вывод сортировки по шагам
print('#^#' * 30)
print(f'3) Сортировка в обратном порядке : {arr}')
