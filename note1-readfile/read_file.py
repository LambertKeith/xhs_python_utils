'''
    作者：Lambert Keith
    日期：2023.10.15
    编码：utf-8
    版本：2023101501
'''
import json

def read_json_file(filename, encoding='utf-8'):
    '''
    读取json文件的函数
    参数：
        filename：需要读取的文件路径
        encoding：编码格式
    输出：
        布尔值：判断是否读取成功
        json内容或者错误信息
    '''
    try:
        with open(filename, 'r', encoding=encoding) as f:
            data = json.load(f)
        return True, data
    except FileNotFoundError:
        print(f"文件 {filename} 未找到。")
        return False, f"文件 {filename} 未找到。"
    except json.JSONDecodeError:
        print(f"无法解析 {filename} 中的JSON。")
        return False, f"无法解析 {filename} 中的JSON。"
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return False, f"读取文件时出错: {e}"


import pandas as pd

def read_txt_file(filename, encoding='utf-8'):
    '''
    读取TXT文件的函数
    参数：
        filename：需要读取的文件路径
        encoding：编码格式
    输出：
        布尔值：判断是否读取成功
        文件内容或者错误信息
    '''
    try:
        with open(filename, 'r', encoding=encoding) as f:
            data = f.read()
        return True, data
    except FileNotFoundError:
        print(f"文件 {filename} 未找到。")
        return False, f"文件 {filename} 未找到。"
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return False, f"读取文件时出错: {e}"

def read_csv_file(filename):
    '''
    读取CSV文件的函数
    参数：
        filename：需要读取的文件路径
    输出：
        布尔值：判断是否读取成功
        CSV数据或者错误信息
    '''
    try:
        data = pd.read_csv(filename)
        return True, data
    except FileNotFoundError:
        print(f"文件 {filename} 未找到。")
        return False, f"文件 {filename} 未找到。"
    except pd.errors.ParserError:
        print(f"无法解析 {filename} 中的CSV。")
        return False, f"无法解析 {filename} 中的CSV。"
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return False, f"读取文件时出错: {e}"

def read_excel_file(filename):
    '''
    读取Excel文件的函数
    参数：
        filename：需要读取的文件路径
    输出：
        布尔值：判断是否读取成功
        Excel数据或者错误信息
    '''
    try:
        data = pd.read_excel(filename)
        return True, data
    except FileNotFoundError:
        print(f"文件 {filename} 未找到。")
        return False, f"文件 {filename} 未找到。"
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return False, f"读取文件时出错: {e}"
