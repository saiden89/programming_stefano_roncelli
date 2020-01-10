#1
a = [4, 8, -9, 'the']
b = ['silent force', 4.67, 9]
print(a + b)

#2
c = '23|64|354|-123'
def string_split(str, sep):
    ls = str.split(sep)
    ls = [int(x) for x in ls] #this is beca we want the elements of the list to be integers and not strings
    return ls

#3
def addlist(l):
    sum = 0
    for i in l:
        sum += i
    return sum

#4
final_sum = addlist(string_split(c, "|")) #here we call the two functions in sequence c
print(final_sum)

#5
def partial_sum(numlist):
    sum = 0
    sum_list = []
    for i in numlist:
        sum += i
        sum_list.append(sum)
    return sum_list

lista = [2, 4, 6 ,7, 3]
partial_sum(lista)

#6
def  square_print(n):
    for i in range(n):
        print('#' * n)
print(square_print(5))

#7
for r in range(1, 11):
    for c in range(1, 11):
        print(c * r, end = ' ') #by default, after every print statement there is a new line (\n). with end we specify that the print should end with a space
    print('\n')