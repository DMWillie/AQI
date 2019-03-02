"""
    作者:北辰
    日期:07/07/2018
    功能:AQI计算
    版本:1.0
"""

def cal_linear(iaqi_lo,iaqi_hi,bp_lo,bp_hi,cp):
    """
    范围缩放
    """
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi

def cal_pm_iaqi(pm_val):
    """
    计算PM2.5的IAQI
    """
    if 0<= pm_val < 36:
        iaqi = cal_linear(0,50,0,35,pm_val)
    elif 36<= pm_val < 76:
        iaqi = cal_linear(50,100, 35, 75, pm_val)
    elif 76<= pm_val < 116:
        iaqi = cal_linear(100,150, 75, 115, pm_val)
    elif 116<= pm_val < 151:
        iaqi = cal_linear(150,200, 115, 150, pm_val)
    elif 151<= pm_val < 251:
        iaqi = cal_linear(200,300, 150, 250, pm_val)
    elif 251<= pm_val < 351:
        iaqi = cal_linear(300,400, 250, 350, pm_val)
    elif 351<= pm_val < 501:
        iaqi = cal_linear(400,500, 350, 500, pm_val)
    return iaqi

def cal_CO_iaqi(CO_val):
    """
    计算CO的IAQI
    """
    if 0<= CO_val < 3:
        iaqi = cal_linear(0,50,0,2,CO_val)
    elif 3<= CO_val < 5:
        iaqi = cal_linear(50,100, 2, 4, CO_val)
    elif 5<= CO_val < 15:
        iaqi = cal_linear(100,150, 4, 14, CO_val)
    elif 15<= CO_val < 25:
        iaqi = cal_linear(150,200, 14, 24, CO_val)
    elif 25<= CO_val < 37:
        iaqi = cal_linear(200,300, 24, 36, CO_val)
    elif 37<= CO_val < 49:
        iaqi = cal_linear(300,400, 36, 48, CO_val)
    elif 49<= CO_val < 61:
        iaqi = cal_linear(400,500, 48, 60, CO_val)
    return iaqi

def cal_aqi(param_list):
    """
    AQI计算
    """
    pm_val = param_list[0]
    CO_val = param_list[1]

    pm_iaqi = cal_pm_iaqi(pm_val)
    CO_iaqi = cal_CO_iaqi(CO_val)

    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(CO_iaqi)

    AQI = max(iaqi_list)
    return AQI

def main():
    """
    主函数
    """
    print('请输入以下信息:用空格分割 ')
    input_str = input('(1)PM2.5 (2)CO: ')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    CO_val = float(str_list[1])

    param_list = []
    param_list.append(pm_val)
    param_list.append(CO_val)
    # 调用AQI计算函数
    AQI_val = cal_aqi(param_list)
    print('空气质量指数为:{}'.format(AQI_val))

if __name__=='__main__':
    main()