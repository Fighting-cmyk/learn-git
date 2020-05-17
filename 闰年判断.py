#闰年判断
def specialyear(year):
    if year%4==0:
        print('{}年是闰年'.format(year))
    else:
        print('{}年2019不是闰年'.format(year))
year=int(input('请输入年份：'))
specialyear(year)
