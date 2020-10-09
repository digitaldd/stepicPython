'''Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.'''
import requests
firstLink = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt').text
link = "https://stepic.org/media/attachments/course67/3.6.3/"
flag = False
count = 0
stringResult = ""
while not flag:
    count += 1
    firstLink = requests.get(str(link + firstLink)).text
    if (str(firstLink).count('txt') < 1) | (count == 300):
        flag = True
        stringResult = str(firstLink)
        print(stringResult)
    print(firstLink)
print(stringResult)