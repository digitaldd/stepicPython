'''Недавно мы считали для каждого слова количество его вхождений в строку.
 Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
 и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
 Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3
'''

def makeDict(list):
    list1 = list
    dict = {}
    countResult = 0
    for x in list1:
        count = list1.count(x)
        if countResult < count:
            countResult = count
        if (dict.get(count) == None) | (str(dict.get(count)) > x):
            dict.update({count: x})
    return dict, countResult

string = ""
with open('/Users/mk/Documents/temp/dataset_3363_3-3.txt', 'r') as strO:  # open the file from Mac for reading only
    for line in strO:
        string += line.strip()  # reading all lines in string
strO.close()  # close the file
list = []
dict = {}
tempStr = ""
count = -1
indexResult = 0
for x in string.lower():
    count += 1
    if x != " ":
        tempStr += x
    if (x == " ") | (count == (len(string) - 1)):
        list.append(tempStr)
        tempStr = ""
dict, indexResult = makeDict(sorted(list))
stringAnswer = str(dict.get(indexResult)) + " " + str(indexResult)
strC = open('/Users/mk/Documents/temp/result4.txt', 'w')  # open the empty file for writing
strC.write(stringAnswer)  # write the result in file
strC.close()  # close the file with result