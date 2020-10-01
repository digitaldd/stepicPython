'''Sample Input:
a10b4c2e10b1  from a file
Sample Output:
aaabbbbcceeeeeeeeeeb  in new file'''

strO = open('/Users/mk/Documents/temp/dataset_3363_2-2.txt','r') # open the file from Mac for reading only
string = strO.readline()  # reading first line
strO.close()  # close the file
strResult = ""
char = ""
index = 0
numb = "0"
for x in range(index, len(string)):
    if string[x].isnumeric():
        for y in range(x, len(string)):
            if string[y].isnumeric():
                numb += string[y]
            else:
                index = y
            if y == len(string) -1 :
                strResult += int(numb) * char
            break
    else:
        strResult += int(numb) * char
        char = string[x]
        numb = "0"
strC = open('/Users/mk/Documents/temp/result.txt','w') # open the empty file for writing
strC.write(strResult) # write the result in file
strC.close()  # close the file with result
print(strResult)  # for checking only