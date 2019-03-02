"""
    作者:北辰
    日期:08/07/2018
    功能:从JSON文件中挑选出AQI最小的5个地区
    版本:2.0
"""

import json

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
    top5_list = city_list[:5]
    # 写入JSON文件
    f = open('top5_aqi.json',mode='w',encoding='utf-8')
    json.dump(top5_list,f,ensure_ascii=False)
    f.close

if __name__=='__main__':
    main()