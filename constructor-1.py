#parametrized constructor:

class student:
    def __init__(self,n,r,id,lst):
        self.name=n
        self.rollno=r
        self.id=id
        self.marks=lst
    def details(self):
        print('my name is:',self.name)
        print('my rollno is:',self.rollno)
        print('my id is:',self.id)
        print('my marks are:',self.marks)

lst=[23,45,67]
s1=student('tharun',290,21,lst)
s1.details()