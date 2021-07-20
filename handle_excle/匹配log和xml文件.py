import os
import xml.etree.ElementTree as ET

path_log = '/Volumes/ShareFiles/99其他/logs'  # 目录下多个log文件
path_xml = '/Volumes/ShareFiles/99其他/xml/000166-20210131-sjqd.xml'  # 指定xml文件路径



def read_logs():
    files = os.listdir(path_log)  # 得到文件夹下的所有文件名称
    s = []
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            f = open(path_log + "/" + file)  # 打开文件
            iter_f = iter(f)  # 创建迭代器
            str = ""
            for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                line = line.replace('\n', '|')
                str += line
            s.append(str)  # 每个文件的文本存到list中

    append_arr(s, 0, 4, 'arr_logs')


def read_xml():
    s = []
    tree = ET.parse(path_xml)
    root = tree.getroot()

    for i in range(len(root[1][0])):
        data = root[1][0][i]  # Table标签所表示的数据
        st = ''
        for child in data.getchildren():
            st += str(child.text) + '|'  # 获取标签内容拼接为字符串插入到列表中
        s.append(st)
    # 调用添加到数组的方法
    append_arr(s, 6, 4, 'arr_xml')
    # print(arr_xml)


def append_arr(s, arr1, arr2, result_arr):
    """
    s：要分析的字符串；
    arr1: 获取表名所在的索引位置
    arr2: 获取数据条数所在的索引位置
    result_arr:最终写入的数组
    """
    global arr_logs
    global arr_xml
    arr = ''
    # 提取s文档中的表名和数据条数
    for m in range(0, len(s)):
        log = s[m].split('|')
        table_name = log[arr1].split('-')[1]  # 获取表名
        file_count = log[arr2]  # 获取文件内条数
        arr += (str(table_name) + '-' + str(file_count) + ',')
    if result_arr == 'arr_logs':
        arr_logs = arr.strip(',')
        # print(arr_logs)
    else:
        arr_xml = arr.strip(',')
        # print(arr_xml)


def compare(arr_logs, arr_xml):
    """
    :return:
    """
    # 遍历logs文件
    logs = arr_logs.split(',')  # 字符串转化为列表
    xml = arr_xml.split(',')  # 字符串转化为列表
    result = '差值' +'\t'+ '表名--log中数量--xml中数量'+'\n'  # 最终结果
    for i in range(len(logs)):  # 遍历log文件
        table_log = logs[i].split('-')
        log_name = table_log[0]
        log_count = table_log[1]
        for j in range(len(xml)):  # 遍历xml文件，并与log文件中通表名的数据进行比对
            table_xml = xml[j].split('-')
            xml_name = table_xml[0]
            xml_count = table_xml[1]
            if log_name == xml_name:
                # 差值 + 表名 + log中数量 + xml中数量
                result += str(
                    int(log_count) - int(xml_count)) + '\t' + log_name + '-' + log_count + '-' + xml_count + '\n'
    print(result)


if __name__ == '__main__':
    read_logs()
    # time.sleep(3)
    read_xml()
    compare(arr_logs, arr_xml)
