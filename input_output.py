#Input Example
name, age = [i for i in input('Enter name and age:').split()]
#Output Example
print('Hello "{}", Your age is {}'.format(name,age))
print('Hello %s, Your age is %s' %(name, age))
print('Hello',name,'Your age is',age)
