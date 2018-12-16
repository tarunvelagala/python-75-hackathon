# defining local and global scope
# global scope
n = int(input("Enter a number"))


def function():
    # local scope
    n = 10
    print('Loacal Scope ---> n value =  ', n)


function()
print('Global Scope  ---> n value', n)
