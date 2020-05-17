#质数判断
def zhishu(count):
    for i in range(2,count//2):
        if count%i==0:
            print('{}不是质数'.format(count))
            break
    else:
        print('{}是质数'.format(count))
count=int(input('请输入要判断的数字：'))
zhishu(count)