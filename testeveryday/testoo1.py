from types import MethodType
class Student(object):
    def set_age(self, age):
        self.age = age
        return self.age

s= Student()
s.name='jack'
print s.name
r= s.set_age(25)
print (r)