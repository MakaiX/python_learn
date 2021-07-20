import datetime

from pymongo import MongoClient

host = '192.168.25.129'
client = MongoClient('mongodb://192.168.25.129:27017/')
table = client['db1']['emp']

l_data = [
    ('张飞', 'male', 18, '20170301', '', 7300.33, 401, 1),  # 以下是教学部
    ('张云', 'male', 78, '20150302', 'teacher', 1000000.31, 401, 1),
    ('刘备', 'male', 81, '20130305', 'teacher', 8300, 401, 1),
    ('关羽', 'male', 73, '20140701', 'teacher', 3500, 401, 1),
    ('曹操', 'male', 28, '20121101', 'teacher', 2100, 401, 1),
    ('诸葛亮', 'female', 18, '20110211', 'teacher', 9000, 401, 1),
    ('周瑜', 'male', 18, '19000301', 'teacher', 30000, 401, 1),
    ('司马懿', 'male', 48, '20101111', 'teacher', 10000, 401, 1),
    ('袁绍', 'female', 48, '20150311', 'sale', 3000.13, 402, 2),  # 以下是销售部门
    ('张全蛋', 'female', 38, '20101101', 'sale', 2000.35, 402, 2),
    ('鹌鹑蛋', 'female', 18, '20110312', 'sale', 1000.37, 402, 2),
    ('王尼玛', 'female', 18, '20160513', 'sale', 3000.29, 402, 2),
    ('我尼玛', 'female', 28, '20170127', 'sale', 4000.33, 402, 2),
    ('杨过', 'male', 28, '20160311', 'operation', 10000.13, 403, 3),  # 以下是运营部门
    ('小龙女', 'male', 18, '19970312', 'operation', 20000, 403, 3),
    ('郭靖', 'female', 18, '20130311', 'operation', 19000, 403, 3),
    ('黄蓉', 'male', 18, '20150411', 'operation', 18000, 403, 3),
    ('梅超风', 'female', 18, '20140512', 'operation', 17000, 403, 3)
]



for n, item in enumerate(l_data):
    d = {
        "_id": n,
        'name': item[0],
        'sex': item[1],
        'age': item[2],
        'hire_date': datetime.datetime.strptime(item[3], '%Y%m%d'),
        'post': item[4],
        'salary': item[5]
    }


    # table.insert_one(d)

# 查询name like 张%的人
results = table.find({'name': {'$regex': '^张'}})
print("11111")
# 利用管道查找对应post
agg1 = table.aggregate([
    {"$match": {
        "$and": [
            {"_id": {"$gt": 3}},
            {"_id": {"$lte": 12}}
        ]
    }
    }, {
        "$project": {
            "name": 1, "post": 1, "_id": 0,
            "new_salary": {
                "$multiply": ["$salary", 100]
            }
        }
    }
])

# 计算每位员工工作年份
agg2 = table.aggregate([{"$project": {"name": 1, "workTime": {"$year": "$hire_date"}}}])

# 计算每位员工的工作年限
agg3 = table.aggregate(
    [{"$project": {"_id": 0, "name": 1,
                   "hire_period": {"$subtract": [{"$year": datetime.datetime.now()}, {"$year": "$hire_date"}]}}}])

# 分组
agg4 = table.aggregate(
    [
        {"$match": {"_id": {"$gte": 1}}},
        # {"$group": {"_id": "$post", "counter": {"$sum": 1}, "avg_salary": {"$avg": "$salary"}}},
        {"$group": {"_id": {"sex": "$sex", "age": "$age"}, "counter": {"$sum": 1},
                    "avg_salary": {"$avg": "$salary"}}},
        {"$project": {"_id": 1, "counter": 1, "avg_salary": 1}},
        {"$match": {"avg_salary": {"$gt": 1000}}},
        {"$sort": {"age": -1}}
    ])

# 取平均工资最高的前两个部门
agg5 = table.aggregate(
    [{"$group": {"_id": "$post", "total_salary": {"$sum": "$salary"}}},
     {"$sort": {"total_salary": -1}},
     {"$limit": 3},
     {"$skip": 1}
     ])
# 随机取n条数据
agg6 = table.aggregate([{"$sample": {"size": 4}}])
print("22222")
print(datetime.date.today())
for i, n in enumerate(agg6):
    print(n)
