# coding=utf-8
import xlwt


class ExcelProcess():

    @staticmethod
    def write_excel(list_1, prefix, filename, pagenum):
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet('My Worksheet')
        head = ['关键词', 'url', '标题', '详情', '回复1', '回复2', '回复3', ]
        for i in range(len(head)):
            worksheet.write(0, i, label=head[i])
        for l in range(1, len(list_1) + 1):
            row_list = list_1[l - 1].split('\t')
            for m in range(len(row_list)):
                worksheet.write(l, m, label=row_list[m])
        workbook.save(prefix + '_' + filename + str(pagenum) + '.xls')

    def write(self, txt__file__path, prefix, filename, num):
        with open(txt__file__path, 'r') as f:
            lines = f.readlines()
        # 求生成Excel 文件个数
        if len(lines) % int(num) == 0:
            excel_file_num = len(lines) / int(num)
        else:
            excel_file_num = int(len(lines) / int(num)) + 1
        for i in range(1, int(excel_file_num) + 1):
            if i == excel_file_num:
                self.write_excel(lines[(i - 1) * int(num):], prefix, filename, str(i))
            else:
                self.write_excel(lines[(i - 1) * int(num):i * int(num)], prefix, filename, str(i))


ex = ExcelProcess()
# 参数说明： txt路径 生成Excel前缀  生成Excel文件名 每个Excel写入行数
ex.write('/Users/js/Desktop/tools/file/000000_0', 'xywy', 'post', 5000)
