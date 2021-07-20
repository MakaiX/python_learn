import re

tels = ["13100001234", "18912344321", "10086", "18800007778"]

for tel in tels:
    ret = re.match("1\d{9}[0-35-68-9]", tel)
    if ret:
        print(ret.group())
    else:
        print("%s 不是想要的手机号" % tel)
ret = re.sub(r"\d+", '1', "python = 997")
print(ret)


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


ret = re.sub(r"\d+", add, "python = 997")
print(ret)

ret = re.sub(r"\d+", add, "python = 99")
print(ret)

re_search = re.search(r"\d+", "我的世界999 00 123")

re_search.group()

test_str = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'

# sub = re.sub(r"<[^>]*>|&nbsp;|\n", "", test_str)
re_sub = re.findall(r'https://.*\.jpg', test_str)
print(re_sub)

regex = r'[1-9][0-9]{5}(\d{4})(\d{2})(\d{2})[0-9]{3}[0-9X]'
p = re.compile(regex)
print(p)
str = '11010019950807532X'
m = p.match(str)
print(m)
print(m.groups())
m.group(1)
