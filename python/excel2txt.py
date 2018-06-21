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
            if j == 0:
                str_ += worksheet.cell_value(i, j).replace('\t','<-t->').replace('\n','<-n->').replace('\r','<-r->')
            else:
                str_ += '\t' + worksheet.cell_value(i, j).replace('\t', '<-t->').replace('\n', '<-n->').replace('\r','<-r->')
        with open(output_path,'a') as f:
            f.write(str_ +'\n')

if __name__ =="__main__":
    read03Excel('/Users/js/Desktop/tools/file/华为-关键词.xlsx','/Users/js/Desktop/tools/file/华为-关键词.txt')