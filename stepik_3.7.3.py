'''На вход программе первой строкой передаётся количество d известных нам слов, после чего на
d строках указываются эти слова. Затем передаётся количество l строк текста для проверки, после чего l строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the'''
listWords, listLines, listAnswer = [], [], []
words = int(input())
for i in range(words):
    listWords.append(input("").lower())

lines = int(input())
listString = ""
for i in range(lines):
    listString += input("").lower() + " "
listLines = listString.split(" ")

for word in range (len(listLines)-1):
    if (listWords.count(listLines[word]) == 0) & (listAnswer.count(listLines[word]) == 0):
        listAnswer.append(listLines[word])

for k in listAnswer:
    print(k)