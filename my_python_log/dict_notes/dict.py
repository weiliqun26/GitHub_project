# 一、字典的创建
# 1.使用大括号{}创建字典
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)
# 空字典
empty_dict = {}
print(empty_dict)

# 2.使用dict()构造函数创建字典
# 通过关键字创造字典
person = dict(name="Bob", age=25, city="Los Angeles")
print(person)
# 通过键值对元组列表创造字典
fruit_dict = dict([("apple", 1), ("banana", 2), ("cherry", 3)])
print(fruit_dict)
# 通过键值对列表创造字典
color_dict = dict(zip(["red", "green", "blue"], [255, 128, 0]))
print(color_dict)
# 通过复制创建字典
copied_dict = dict(my_dict)
print(copied_dict)

# 3.使用字典推导式创建字典
squared_dict = {x: x**2 for x in range(1, 5)}
print(squared_dict)

# 二、字典的基本操作
# 1.访问字典中的值
print(my_dict["name"])  # 通过键访问值
print(my_dict.get("age"))  # 使用get()方法访问值
print(my_dict.get("country", "USA"))  # 使用get()方法访问不存在的键，提供默认值‘

# 三、添加和修改元素
# 1.通过[]添加或修改元素
my_dict["age"] = 31  # 修改已有键的值
my_dict["country"] = "USA"  # 添加新键值对
print(my_dict)
# 2.使用update()方法添加或修改元素
my_dict.update({"city": "San Francisco", "profession": "Engineer"})
print(my_dict)
# 四、删除元素
# 1.使用del语句删除元素
del my_dict["profession"]
print(my_dict)
# 2.使用pop()方法删除元素并返回值
age = my_dict.pop("age")
print(f"Removed age: {age}")
print(my_dict)
# 3.使用popitem()方法删除并返回最后插入的键值对
last_item = my_dict.popitem()
print(f"Removed item: {last_item}")
print(my_dict)
# 4.使用clear()方法清空字典
my_dict.clear()
print(my_dict)
# 五、字典的遍历
# 1.遍历字典的键
sample_dict = {"a": 1, "b": 2, "c": 3}
for key in sample_dict:
    print(f"Key: {key}")
# 2.遍历字典的值
for value in sample_dict.values():
    print(f"Value: {value}")
# 3.遍历字典的键值对
for key, value in sample_dict.items():
    print(f"Key: {key}, Value: {value}")

# 六、字典的其他常用方法
# 1.使用keys()方法获取所有键
keys = sample_dict.keys()
print(f"Keys: {list(keys)}")
# 2.使用values()方法获取所有值
values = sample_dict.values()
print(f"Values: {list(values)}")
# 3.使用items()方法获取所有键值对
items = sample_dict.items()
print(f"Items: {list(items)}")
# 4.使用setdefault()方法获取值，如果键不存在则添加键值对
value = sample_dict.setdefault("d", 4)
print(f"Setdefault value: {value}")
print(sample_dict)
# 5.使用copy()方法创建字典的浅拷贝
shallow_copy = sample_dict.copy()
print(f"Shallow copy: {shallow_copy}")
# 6.使用fromkeys()方法创建新字典
new_dict = dict.fromkeys(["x", "y", "z"], 0)
print(f"New dict from keys: {new_dict}")
