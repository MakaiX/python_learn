from redis import *

try:
    sr = StrictRedis(host='192.168.25.129', port=6379, db=0)
    sr.set('aa', 'hala')
    print(sr.get('aa'))
except Exception as e:
    print(e)
