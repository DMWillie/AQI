"""
    作者:北辰
    日期:09/07/2018
    功能:AQI计算
    版本:4.0
    4.0新增功能:判断输入的文件是JSON文件还是CSV文件
"""

import json
import csv
import os

def process_json_file(filepath):
    """
    解码JSON文件
    """
    # f = open(filepath, mode='r', encoding='utf-8')
    # city_list = json.load(f)
    with open(filepath,mode='r',encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)

def process_csv_file(filepath):
    """
    处理CSV文件
    """
    with open(filepath, mode='r', encoding='utf-8',newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row)) # 使得每一行列表里的元素用逗号连接起来

def main():
    """
    主函数
    """
    filepath = input('请输入文件名称: ')
    # os模块的splitext函数将路径分割成文件名和扩展名
    filename , file_ext = os.path.splitext(filepath)

    #判断文件格式
    if file_ext == '.json':
        # JSON文件
        process_json_file(filepath)
    elif file_ext == '.csv':
        # csv文件
        process_csv_file(filepath)
    else:
        print('不支持的文件格式!')



if __name__=='__main__':
    main()