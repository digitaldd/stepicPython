'''Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
Программа принимает на вход две строки одинаковой длины, на первой строке записаны
символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт
строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра.
Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:
*d*%*d*#*d*
dacabac

Sample Input 2:
dcba
badc
dcba
badc
Sample Output 2:
badc
dcba'''

stringNormal, stringCrypt, strForCrypt, strForDecrypt = input(""), input(""), input(""), input("")
stringCrypted, stringDecrypted = "", ""
for i in strForCrypt:
    index = stringNormal.index(i)
    stringCrypted += stringCrypt[index]
print(stringCrypted)

for i in strForDecrypt:
    index = stringCrypt.index(i)
    stringDecrypted += stringNormal[index]
print(stringDecrypted)