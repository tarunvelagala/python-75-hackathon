#empty dictionary
my_dict1={}
print(type(my_dict1))

#dictionary with integer keys
my_dict2={1:"bigdata",2:"hadoop"}
print(type(my_dict2))

#dictionary woth mixed keys
my_dict3={"name":"tarun",1:[95,92,94]}
print(type(my_dict3))

keys={'a','e','i','o','u'}
value="vowel"
vowels=dict.fromkeys(keys,value)
print(vowels)
