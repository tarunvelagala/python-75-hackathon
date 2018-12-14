fib= lambda n: n if n<=1 else fib(n-1) +fib(n-2)
n, i = int(input('enter upto which number')), 0
while i<n-1:
    print(fib(i))
    i+=1

