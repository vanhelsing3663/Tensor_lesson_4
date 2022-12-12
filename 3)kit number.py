from random import randint

'''Заполнить два случайных набора чисел. Вывести оба набора. Указать какие элементы:
1)входят одновременно в оба;
2)входят только в первое, но не входят во второе;
3)входят только во второе, но не входят в первое;
4)входят в первое или во второе, но не в оба из них одновременно.'''

lenght_1 = randint(1, 20)
lenght_2 = randint(1, 20)
multiplicity_1 = {randint(1, 10) for i in range(lenght_1)}
multiplicity_2 = {randint(1, 10) for i in range(lenght_1)}
print(f'Два случайных набора различной длины :\n1) {multiplicity_1}\n2) {multiplicity_2}')


