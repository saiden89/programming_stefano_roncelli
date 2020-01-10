#1
a = "fire and ice"

#2
print(a[2])

#3
print(a[4])

#4
print(a[10], a[-1], a[-2])

#5
print(a[1::2])

#6
print(a[::2])

#7
print(a[:len(a)//2])

#8
print(a[::-1])

#9
print(a.count('e'))
print(a.count('i'))

#10
print(a.replace('and', '&'))

#11
print(a.find('fire'))

#12
print(a.find('re and'))

#13
print(a.find('re &'))

#14
print(a.find('e'))

#15
print(a.rfind('e')) #same as find, but starts from the right