#coding:utf-8

import sys
reload(sys)   
sys.setdefaultencoding('utf8')
import xlrd

def read03Excel(input_path,output_path):
    workbook = xlrd.open_workbook(input_path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    print(worksheet)
    for i in range(0, worksheet.nrows):
        # row = worksheet.row(i)
        str_ = ""
        for j in range(0, worksheet.ncols):
            tempValue = worksheet.cell_value(i, j)
#             if isinstance(tempValue,(float)): #excel中的整型会被读取为浮点型，根据需要在这里进行转换
#                 tempValue = int(tempValue)
            if j == 0:
                str_ += str(tempValue).replace('\t','<-t->').replace('\n','<-n->').replace('\r','<-r->')
            else:
                str_ += '\t' + str(tempValue).replace('\t', '<-t->').replace('\n', '<-n->').replace('\r','<-r->')
        with open(output_path,'a') as f:
            f.write(str_ +'\n')

if __name__ =="__main__":
    #支持中文路径，但是python2时Windows下不能使用命令行传入中文路径
    # excelPath,textPath = sys.argv[1],sys.argv[2] #纯英文路径时可以使用命令行传入参数
    excelPath = 'C:\Users\manin\Desktop\搜狗499054数据/0.xlsx'
    textPath = 'C:\Users\manin\Desktop\搜狗499054数据/0.txt'
    read03Excel(excelPath.decode('utf-8'), textPath.decode('utf-8'))