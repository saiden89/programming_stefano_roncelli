#1
def increase(n):
	return(n+1)

#2
def add(x, y):
	return x+y

#3
def add3(x, y, z):
	return(x, y, z)

#4
def add5(x, y, z, a, b):
	return(x+y+z+a+b)

#5
def numstr(s, n):
	return s*n

#6
def numstr(s, n):
	s=s+","
	concat=s*n 
	return concat[:-1]
prova=numstr("ciao", 5)
print(prova)

#7
def numstr(s, n, sep):
	s=s+sep
	concat=s*n
	return concat[:-1]