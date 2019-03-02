"""
    作者:北辰
    日期:08/07/2018
    功能:AQI计算
    版本:3.0
    3.0新增功能:将AQI数据写入CSV文件
"""

import json
import csv

def process_json_file(filepath):
    """
    解码JSON文件
    """
    f = open(filepath,mode='r',encoding='utf-8')
    city_list  = json.load(f)
    return city_list

def main():
    """
    主函数
    """
    filepath = input('请输入JSON文件名称: ')
    city_list = process_json_file(filepath)
    # 对city进行排序,排序方法按照aqi的值从小到大(lambda函数)
    city_list.sort(key=lambda city:city['aqi'] )

    lines = []
    # 列名
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))
    # print(lines)
    f = open('aqi.csv','w',encoding='utf-8',newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()

if __name__=='__main__':
    main()