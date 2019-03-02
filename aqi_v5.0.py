"""
    作者:北辰
    日期:09/07/2018
    功能:利用网络爬虫获取相关的数据
    版本:5.0
"""

import requests

def get_html_text(url):
    """
    返回url的文本
    """
    r = requests.get(url,timeout=30)
    # print(r.status_code)
    return r.text

def main():
    """
    主函数
    """
    city_pinyin = input('请输入城市拼音: ')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)
    # 网页标签
    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 3
    # 获取索引
    aqi_val = url_text[begin_index:end_index]
    print('空气质量为:{}'.format(aqi_val))

if __name__=='__main__':
    main()