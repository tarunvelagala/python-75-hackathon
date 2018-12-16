a = 0

if a == 0:
    # this is global variable
    b = 1


def fun(c):
    # this is local variable
    d = 3
    print(c)


# call function with value 7
fun(7)

# a and b exist since these are global variables
print(a)
print(b)

# c and d does not exist since local variables cannot be called outside
# print(c)
# print(d)
