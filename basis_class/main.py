# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# # 九九乘法表
# i = 1
#
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d * %d = %d" % (j, i, i * j), end="\t")
#         j += 1
#     print(end="\n")
#     i += 1
#
#
# var = 100
#
# if (var == 100): print("变量 var 的值为100")
#
# print("Good bye!")

# for循环
# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
#     print('当前水果 :', fruits[index]
#           )
#
# print("Good bye!")
# 判断质数
# for num in range(10, 20):
#     for i in range(2, num):
#         if num % i == 0:
#             j = num / i
#             print("%d 等于 %d * %d" % (num, i, j))
#             break
#     else:
#         print("%d 质数" % num)
#
# for letter in 'Python':  # 第一个实例
#     if letter == 'h':
#         continue
#     print
#     '当前字母 :', letter

# localtime = time.localtime(time.time())
# print("本地时间为 :", localtime)
#
# print(time.process_time())
# # 斐波那契数列
# a, b = 0, 1
# while b < 100:
#     print(b, end=' ')
#     a, b = b, a + b
#
# # 迭代器
# list = [1, 2, 3, 4]
# it = iter(list)
# while True:
#     try:
#         print(next(it), end=' ')
#     except StopIteration:
#         sys.exit()


# 生成器
def fibonacci(n):
    a, b, counter = 0, 1, 1
    while True:
        if (n < counter):
            return
        yield b
        a, b = b, a + b
        counter += 1


faction = fibonacci(10)

# while True:
#     try:
#         print(next(faction), end=' ')
#     except StopIteration:
#         sys.exit()

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

newList = [[row[i] for row in matrix] for i in range(4)]

for x in newList:
    print(x)

for i, v in enumerate([1, 2, 3]):
    print(i, v)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

print(dir())