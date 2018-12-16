# set operations
a = {1, 2, 3, 4, 5, 6, 1, 2, 3}
print(set(a))
a.add(11)
a.add(12)
print(a)

# adding tuple to a set
vowels = {'a', 'e', 'u'}
tup = ('i', 'o')
vowels.add(tup)
print('vowels are:', vowels)
