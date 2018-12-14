
lst = []
n= int(input('enter the range '))
for i in range(n):
    x = tuple(i for i in input().split(','))
    lst.append(x)
print(sorted(lst))
