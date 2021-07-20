import cmath
import random

if __name__ == '__main__':
    print('PyCharm')

    # num = input('输入第一个数字:')
    #
    # # 计算实数和复数的平方根
    # if num.__contains__('-') and num.__contains__('.'):  # 负数、浮点数
    #     num_sqrt = cmath.sqrt(float(num))
    #     print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(float(num), num_sqrt.real, num_sqrt.imag))
    # elif num.__contains__('-'):  # 负数
    #     num_sqrt = cmath.sqrt(int(num))
    #     print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
    # else:
    #     if num.__contains__('.'):
    #         num_sqrt = float(num) ** 0.5
    #         print('{0}的平方根为{1:0.3f}'.format(float(num), num_sqrt))
    #     else:
    #         num_sqrt = int(num) ** 0.5
    #         print('{0}的平方根为{1:0.3f}'.format(num, num_sqrt))

random1 = random.randrange(0, 10, 1)
print(random1)


# 判断是否为数字
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (ValueError, TypeError):
        pass


print(isNumber('٥'))


# 判断是否为闰年
def isLeapYear(y):
    y = int(y)
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                print('{0}为世纪闰年'.format(y))
            else:
                print('{0}为平年'.format(y))
        else:
            print('{0}为普通闰年'.format(y))
    else:
        print('{0}为平年'.format(y))


print(isLeapYear('2000'))

lis = [{"name": "Taobao", "age": 100},
       {"name": "Runoob", "age": 7},
       {"name": "Google", "age": 100},
       {"name": "Wiki", "age": 200}]
print("根据age升序--")
print(sorted(lis, key=lambda i: i['age']))

print(sorted(lis, key=lambda i: (i['age'], i['name'])))

print(sorted(lis, key=lambda i: i['age'], reverse=True))
