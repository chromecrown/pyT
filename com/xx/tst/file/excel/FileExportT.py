#coding=utf-8

from pyExcelerator import *

def write2Excel(_lstTuple):
    """
    把参数中指定的数据写入excel
    使用到的lib包:StringIO,xlsxwriter
    参数说明:
    _lstTuple:由tuple元组为元素的list列表
    """
    import StringIO
    import xlsxwriter
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    #向workbook对象中添加数据
    _lenList = len(_lstTuple)
    for row in range(0,_lenList):
        _tuple = _lstTuple[row]
        _lenTuple = len(_tuple)
        for col in range(0,_lenTuple):
            _item = _tuple[col]
            worksheet.write(row,col,_item)
    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data包含了excel文件
    return xlsx_data

def genCSV():
    import csv
    with open('egg2.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['a', '1', '1', '2', '2'])
        spamwriter.writerow(['b', '3', '3', '6', '4'])
        spamwriter.writerow(['c', '7', '7', '10', '4'])
        spamwriter.writerow(['d', '11','11','11', '1'])
        spamwriter.writerow(['e', '12','12','14', '3'])

def wtExcel():
    """
    使用pyExcelerator库写入excel文件
    """
    w = Workbook()#创建一个工作薄
    ws = w.add_sheet("hey,hades")#创建一个工作表
    ws.write(0,0,'bit')
    ws.write(0,1,"huang")#在第1行2列写入huang
    ws.write(1,0,'xuan')#2行1列写入xuan
    w.save("mini.xls")
            
if __name__ == "__main__":
    wtExcel()