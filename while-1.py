#display even number between m and n

m,n=[int(i)for i in input('enter two numbers').split(',')]
while(m<=n):
    print(m,end=' ')
    m=m+2
print('\n')

#dislaying in another way

m=int(input('enter a number'))
n=int(input('enter another number'))
while(m<=n):
    if m%2==0:
        print(m,end=' ')
    m=m+1
print('\n')

#checking before while loop

m=int(input('enter a num'))
n=int(input('enter second num'))
if m%2!=0:
    m+=1
while m<=n:
    print(m,end=' ')
    m+=2