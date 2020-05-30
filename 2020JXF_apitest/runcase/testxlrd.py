#/Users/jiangxufeng1/Desktop/test/fukun_apitest-master/fukun_apitest/data/qq_apiTest.xlsx
#-*- coding: utf-8 -*-
import xlrd
import collections
import  time
class TestXlrd():
    def __init__(self,fileName,SheetName):
        self.fileName = fileName
        self.SheetName = SheetName
    def readxlrd(self):
        data = xlrd.open_workbook(self.fileName)
        table = data.sheet_by_name(self.SheetName)

        nrows = table.nrows
        ncols = table.ncols
        if nrows > 1:
            firstrows = table.row_values(0)
            print(firstrows)
            listdata = []
            for col in range(1, nrows):
                values = table.row_values(col)
                #dict_test = collections.OrderedDict(zip(firstrows, values))
                dict_test = dict(zip(firstrows, values))
                listdata.append(dict_test)
            return listdata
        else:
            print("no data!")
            return None
if __name__ == '__main__':
    s = TestXlrd("/Users/jiangxufeng1/Desktop/qq_apiTest 2.xlsx", "Sheet1")
    x = s.readxlrd()
    now_time= time.time()
    print(now_time)
    timi=str(now_time).split('.')
    timii=str(now_time).split('.')[0]
    print(timi)
    print(timii)
    print(x)

