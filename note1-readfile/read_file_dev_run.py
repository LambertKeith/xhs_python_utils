from read_file import read_csv_file, read_excel_file, read_json_file, read_txt_file


def read_csv_file_test():
    read_csv_file



def read_json_file_test():
    '''
    读取json文件测试
    read_flag用来表示读取操作是否成功
    '''
    read_flag, data = read_json_file(filename='data/test.json')
    if read_flag:
        # 如果读取成功，可以对数据进行操作
        print(data[0]['name'])
    else:
        print("读取错误，错误如下：", data)

read_json_file_test()