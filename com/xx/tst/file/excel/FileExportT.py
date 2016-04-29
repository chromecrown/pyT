#coding=utf-8

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