import json
import calendar


def swapToJson(data):
    json_str = json.dumps(data)
    return json_str


data = {'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com'}

print(repr(data))
print(swapToJson(data))

print(calendar.calendar(theyear=2020, w=2, l=1, c=6))
