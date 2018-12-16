# to check even or odd using simple if
n = int(input('enter a number'))

if n & 1:
    print('Even')
else:
    print('Odd')

# to check even or odd

n = int(input('enter a number'))
if n == 0:
    print(n, 'is zero')
elif n % 2 == 0:
    print(n, 'is even')
else:
    print(n, 'is odd')
