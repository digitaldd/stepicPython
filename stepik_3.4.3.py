'''Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
 где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого
абитуриента записывает его среднюю оценку по трём предметам на отдельной строке, соответствующей
этому абитуриенту, в файл с ответом.
Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам
и добавьте полученные значения, разделённые пробелом, последней строкой в файл с ответом.
В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику
и одной строкой со средними оценками по трём предметам.
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667'''

list = []
with open('/Users/mk/Documents/temp/dataset_3363_2-2.txt', 'r') as strO:  # open the file from Mac for reading only
    for line in strO:
        list.append(line.strip().split(";"))  # reading all lines in string
strO.close()  # close the file
first, second, third, middle, count = 0, 0, 0, 0, 0
stringMiddle = ""
for string in list:
    count += 1
    middle = 0
    first += int(string[1])
    second += int(string[2])
    third += int(string[3])
    stringMiddle += str((int(string[1]) + int(string[2]) + int(string[3])) / 3) + '\n'
strC = open('/Users/mk/Documents/temp/result4.txt', 'w')  # open the empty file for writing
strC.write(stringMiddle)  # write the result in file
strC.write(str(first/count) + " " + str(second/count) + " " + str(third/count) + " ")  # write the result in file
strC.close()  # close the file with result