"""
    作者:北辰
    日期:09/07/2018
    功能:利用网络爬虫获取相关的数据
    版本:7.0
    6.0新增功能:利用BeautifulSoup库解析html
    7.0新增功能:利用爬虫自动获取所有城市的AQI
"""

import requests
from bs4 import BeautifulSoup

def get_city_aqi(city_pinyin):
    """
    获取城市的AQI
    """
    url = 'http://pm25.in/' + city_pinyin
    r= requests.get(url,timeout=30)
    soup = BeautifulSoup(r.text,'lxml')
    div_list = soup.find_all('div',{'class':'span1'})
    city_aqi = []

    # 遍历8次,分别拿到8个指标
    for i in range(8):
        div_content = div_list[i]
        # .text获取标签的内容,.strip()去除中间的空格
        caption = div_content.find('div',{'class':'caption'}).text.strip()
        value = div_content.find('div',{'class':'value'}).text.strip()
        # 将每一个指标的名称和值组成一个元组添加到列表中
        city_aqi.append((caption,value))

    return city_aqi

def get_all_cities():
    """
    获取所有城市列表
    """
    baseurl = 'http://pm25.in'
    city_list = []
    r = requests.get(baseurl, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')

    # 获取city列表所在的标签
    city_div = soup.find_all('div',{'class':'bottom'})[-1]
    city_link_list = city_div.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href']
        city_list.append((city_name,city_pinyin))

    return city_list

def main():
    """
    主函数
    """
    city_list = get_all_cities()
    for city in city_list:
        city_name = city[0]
        city_pinyin = city[1]
        city_aqi = get_city_aqi(city_pinyin)
        print(city_name,city_aqi)

if __name__=='__main__':
    main()