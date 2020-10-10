'''Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются.
Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста
используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый).
Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.
В качестве ответа прикрепите файл с полученными данными о среднем росте.
Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153
Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0'''


def beginList(string1):
    list = []
    string = string1
    for x in range(12):
        list.append(string)
    return list


def fillingLists(list1):
    list = list1
    listAnswer, listCounter = beginList(0), beginList(0)
    for i in list:
        listAnswer[int(i[0])] = listAnswer[int(i[0])] + int(i[2])
        listCounter[int(i[0])] += 1
    return calculateList(listAnswer, listCounter)


def calculateList(list1, list2):
    listAnswer, listCounter = list1, list2
    finalList = beginList("-")
    for i in range(len(listCounter)):
        if (listAnswer[i] > 0):
            finalList[i] = (listAnswer[i] / listCounter[i])
    return finalList


list = []
with open('/Users/mk/Documents/temp/dataset_3380_5.txt', 'r') as strO:  # open the file from Mac for reading only
    for line in strO:
        list.append(line.strip().split("\t"))  # reading all lines in string
strO.close()  # close the file

finalList = fillingLists(list)
for i in range(1, len(finalList)):
    print(i, finalList[i])
