# #Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
              
listnum = []
for i in range(randint(5, 20)): 
    listnum.append(randint(0, 20))

print(f'Сгенерированный список: {listnum}')

newlist =[]
for j in range(len(listnum)):
    for k in range(len(listnum)):
        if j != k and listnum[j] == listnum[k]:
            break
    else:                           # else относится к циклу и будет выполнятся только 1 раз и в последней итерации
        newlist.append(listnum[j])

print(f'Список с исключением повторяющихся элементов: {newlist}')
