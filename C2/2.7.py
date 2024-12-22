import json

data = '{"Ho_va_ten": "Nguyen THi Phanh", "age": 19, "school": "u"}'

obj = json.loads(data)

print(obj)
print(type(obj))