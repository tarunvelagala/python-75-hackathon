#python code to demonstrate Type conversion
#using dict(),complex(),str()

#initializing integers
a=1
b=2

#initializing tuple
tup=(('a',1),('f',2),('g',3))

#printing integer converting to complex numbers
c=complex(1,2)
print("after converting integer to complex number:",end=" ")
print(c)

#printing integer converting to string
c=str(a)
print("after converting integer to string:",end=" ")
print(c)

#printing tuple converting to expression
c=dict(tup)
print("After converting tuple to dictionary:",end=" ")
print(c)