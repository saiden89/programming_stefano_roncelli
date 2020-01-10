# from math import sqrt
# x=7
# print(x)
# y = 3.14
# print(x % 2)
# x/y
# z = 2*x + 1
# x1= 3
# y1=5
# x2=10
# y2=-3

# distance = sqrt(abs((x2-x1)**2+(y2-y1)**2))
# print (distance)
#Exercise 1
def stringloop(s, n):
    for x in range(0,n):
        print(x, s)
        x = x + 1
stringloop("ciao", 5)

#Exercise 2
def basecount(s):
    for x in range(len(s)):
        print("base", x, "is", s[x])
        x=x+1
basecount("ciao")

#Exercise 3
restriction_sites = [
    "GAATTC",#EcoRI
    "GGATCC",#BamHI
    "AAGCTT",#HindIII
]

for enzyme in restriction_sites:
    print(enzyme + " is a restriction site")

#Exercise 4
def check_site(seq):
    for enzyme in restriction_sites:
        print(enzyme + " is in the sequence: ", enzyme in seq)
check_site("ACTGACTACTACTAGCTACTACGGCGCCGCGTACGATCG")

