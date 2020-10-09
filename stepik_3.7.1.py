'''Напишите программу, которая принимает на стандартный вход список игр футбольных команд
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже. Порядок вывода команд произвольный.
Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6'''

dictList1, dictList2 = [], []  # for numbers (2 0 0 2 0)
list, tempList = [], []  # for input
dict = {}  # command's name + dictList

# input start
lines = int(input())
for i in range(lines):
    list.append(input(""))
# input end

for i in range(0, (len(list))):
    tempList = str(list[i]).strip("[']").split(';')  # strip other chars

    if (dict.get(tempList[0]) == None):
        dict.update({tempList[0]: [0, 0, 0, 0, 0]})  # add command and empty list in dict
    if (dict.get(tempList[2]) == None):
        dict.update({tempList[2]: [0, 0, 0, 0, 0]})

    dictList1 = dict.get(tempList[0])
    dictList2 = dict.get(tempList[2])

    if (int(tempList[1])) > (int(tempList[3])):  # if first command win
        dictList1[0] += 1
        dictList1[1] += 1
        dictList1[4] += 3
        dictList2[0] += 1
        dictList2[3] += 1

    if (int(tempList[1])) < (int(tempList[3])):  # if first command lose
        dictList1[0] += 1
        dictList1[3] += 1
        dictList2[0] += 1
        dictList2[1] += 1
        dictList2[4] += 3

    if (int(tempList[1])) == (int(tempList[3])):  # if eq
        dictList1[0] += 1
        dictList1[2] += 1
        dictList1[4] += 1
        dictList2[0] += 1
        dictList2[2] += 1
        dictList2[4] += 1
# output
for k, v in dict.items():
    print((k + ':'), *v)