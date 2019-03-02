"""
    作者:北辰
    日期:09/07/2018
    功能:利用pandas进行数据分析
    版本:9.0
    9.0新增功能:进行数据清洗并可视化
"""

import pandas as pd
import matplotlib.pyplot as plt

# 解决图片中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():
    """
    主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('基本信息如下: ')
    print(aqi_data.info())
    print('数据预览(前5行)')
    print(aqi_data.head())
    # print(aqi_data[['City','AQI']]) 取出'City'和'AQI'这两列数据

    # 数据清洗
    # 只保留AQI>0的数据
    clean_aqi_data = aqi_data[aqi_data['AQI']>0]
    # filter_condition = (aqi_data['AQI']>0)
    # clean_aqi_data = aqi_data[filter_condition]


    # 基本统计
    print('AQI最大值:',clean_aqi_data['AQI'].max())
    print('AQI最小值:', clean_aqi_data['AQI'].min())
    print('AQI均值:', clean_aqi_data['AQI'].mean())

    # top50
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    # 数据可视化
    top50_cities.plot(kind='bar',x='City',y='AQI',title='空气质量最好的50个城市'
                      ,figsize=(20,10))
    plt.savefig('top50_aqi_cities_bar.png')
    plt.show()

    # # bottom10
    # bottom10_cities = clean_aqi_data.sort_values(by=['AQI'],ascending=False).head(10)
    # # bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
    # print('空气质量最差的的10个城市: ')
    # print(bottom10_cities)

    # # 将top10和bottom10城市保存成CSV文件
    # top10_cities.to_csv('top10_aqi.csv',index=False)
    # bottom10_cities.to_csv('bottom10_aqi.csv',index=False)

if __name__=='__main__':
    main()