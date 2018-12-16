#Class Method

class sample:
    x = 10
    @classmethod
    def modify(cls):
        cls.x+=1

s1 = Sample()
s2 = Sample()
print(s1.x,s2.x)

s1.modify()
print(s1.x,s2.x)

s1.x+=1
print(s1.x,s2.x)