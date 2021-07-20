import os
import sys

import cx_Oracle  # 导入数据库

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8'


# 获取类别字典
def get_lb_dict(code):
    fl_name = ''
    if code == 'JC':
        fl_name = '基础指标'
    elif code == 'QD':
        fl_name = '渠道类指标'
    elif code == 'TG':
        fl_name = '投顾指标'
    elif code == 'DS':
        fl_name = '电商指标'
    elif code == 'YY':
        fl_name = '运营指标'
    elif code == 'CW':
        fl_name = '财务指标'
    elif code == 'HG':
        fl_name = '合规指标'
    elif code == 'RS':
        fl_name = '人事机构指标'
    elif code == 'JS':
        fl_name = '精算指标'
    elif code == 'ZG':
        fl_name = '资管指标'

    return fl_name

def parseFile(cursor_oracle, file_Path):
    global define, formula
    file = open(file_Path, 'r', encoding='UTF-8')
    lines = file.readlines()
    insert_line = 0
    if lines:
        for line in lines:
            line = line.strip().split('｜')
            if len(line) != 0:
                fl = get_lb_dict(line[0][0:2])  # 分类
                code_ = line[0]  # 指标编码
                name = line[1]  # 指标名称
                # print(get_lb_dict(line[0][0:2]))
                # 只有定义字段
                if len(line) == 3 and line[2].startswith("定义：", 0):
                    define = line[2].lstrip("定义：")  # 指标定义
                    formula = ''
                # 只有公式字段
                elif len(line) == 3 and line[2].startswith("公式：", 0):
                    define = ''
                    formula = line[2].lstrip("公式：")
                # 包含定义和公式字段
                elif len(line) == 4:
                    define = line[2].lstrip("定义：")  # 指标定义
                    formula = line[3].lstrip("公式：")

                sql = "insert into FR_target_detail(classify, code_, name, define, formula) values (:1,:2,:3,:4,:5)"
                params = (fl, code_, name, define, formula)

                # print(params)
                cursor_oracle.execute(sql, params)
            insert_line += 1
    file.close()
    print('总共插入{}条数据'.format(insert_line))


if __name__ == '__main__':
    # 创建oracle连接
    conn_str = 'stage/User123$@10.50.100.5:1521/HKODSDG'
    connection_oracle = cx_Oracle.Connection(conn_str)
    cursor_oracle = connection_oracle.cursor()

    parseFile(cursor_oracle, '/opt/sjzd/SJZD.txt')
    connection_oracle.commit()  # 提交数据
    cursor_oracle.close()
    connection_oracle.close()


    # 测试创建mysql连接
    # connection_oracle = pymysql.connect(host="hadoop00", port=3306, user="root", passwd="mark1005", db="test",
    #                                     charset="utf8mb4")
    # 使用cursor()方法获取操作游标
    # cursor_oracle = connection_oracle.cursor()

    # parseFile(cursor_oracle, './SJZD.txt')  # 调用文本解析方法，插入数据