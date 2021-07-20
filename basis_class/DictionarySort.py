import time


def dictionairy():
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("按键(key)排序:")
    for i in sorted(key_value):
        print("{0}--{1}  ".format(i, key_value[i]))

    print("按值(value)排序:")
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))


def Merge(dic1, dic2):
    return (dic1.update(dic2))


dic1 = {"a": 5, "b": 8}
dic2 = {"c": 10, "d": 200}
print(Merge(dic1, dic2))
print(dic1)

# 时间转换
a1 = "2019-5-10 23:40:00"
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")

time_time = int(time.mktime(timeArray))
print(timeArray)
print(time_time)


def main():
#    dictionairy()
    pass

if __name__ == '__main__':
    main()
