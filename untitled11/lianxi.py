import os, sys
d ={'a':[{'id':1, 'name':'hongmi', 'status':1}, {'id':2, 'name':'hongmipro', 'status':2}], 'b':[{'id':11, 'reaname':'huaweimate', 'restatus':20},{'id':21, 'reaname':'huaweipro', 'restatus':20}]}
print(d.items())
def test():
    for table, data in d.items():
        print ("this is table:", table)
        for p in data:
            print("data is print:", p)


test()

print(__file__)
parentdiy=os.path.abspath(__file__)
print(parentdiy)
parentdit=os.path.dirname(os.path.abspath(__file__))
print(parentdit)
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parentdir)