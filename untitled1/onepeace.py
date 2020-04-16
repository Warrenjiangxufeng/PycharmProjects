#def greet_user(username):
 #    print("hello,"+username.title()+"!")
#reet_user("jiang")
#
def describe_pet(pet_type,pet_name):

    print("\nI have a "+pet_type+".")
    print("my"+pet_type+ "'s name is"+pet_name.title()+".")
describe_pet('dog','xiaohui')

def get_formatted_name(petfirstname_name,last_name):
    fullname_pet=petfirstname_name+''+last_name
    return fullname_pet.title()
dogblack = get_formatted_name('herry','black')
print(dogblack)

def getfull_name(firstname,secondname,thirdname):
    fullnameman=firstname+''+secondname+''+thirdname
    return fullnameman.title()
jackname=getfull_name('mading','lude','jin')
print(jackname)

def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
z=power(7,3)
print(z)

d={'a':1,'b':2,'c':4}
for g in d:
    print(g)
for h in d.itervalues():
    print(h)

for i,j in d.iteritems():
    print(i,j)
for io in 'Awhor':
    print(io)
for kh ,vh in enumerate(['ai','bi','nh']):
    print kh,vh
mom=[(1,1),(1,5),(2,4)]
for x,y in mom:
    print(x,y)
f=lambda x:x*(x+1)
print(f(5))


def build(l,v):
    return lambda :l*l+v*v
print build(2,3)()



class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
jx=Student('xufeng',100)

def print_score(st):
    print('%s' % (st.score))

print_score(jx)

class teacher(object):
    def __init__(self,t_name,t_score):
        self.t_name=t_name
        self.t_score=t_score
    def print_name(mk):
        print('%s' % (mk.t_name))

tn=teacher('zhou',98)
tn.print_name()

class annimal(object):
    def run(self):
        print("Annimal is running!")

xdog=annimal()
xdog.run()

class Dog(annimal):
    def run(self):
        print('dog is talk')

class Cat(annimal):
    pass
ydog=Dog()
ydog.run()
zcat=Cat()
zcat.run()

from  datetime import datetime
now = datetime.now()
print(now)

dt = datetime(2018,11,15,12,20)
print(dt)
print(dt.strftime('%a, %b %c %d:%e'))


test = {'wang':1,'jiang':13,'zhou':44}
test2 = ['dog','fish','potato']
test3 = ('sisiter','brother','father')

test2.append('jiang')
test2.insert(1,'wu')
print (test2)

print (test['wang'])
print(test.get('zheng',0))
test.pop('wang')
print(test)