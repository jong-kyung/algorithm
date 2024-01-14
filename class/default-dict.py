from collections import defaultdict

my_dict1 = defaultdict(int)
my_dict2 = defaultdict(str)
my_dict3 = defaultdict(list)
my_dict4 = defaultdict(set)

print(my_dict1)
print(my_dict2)
print(my_dict3)
print(my_dict4)

# 키 에러
my_dict5 = dict()
# print(my_dict5['my_key']) # 없는 key를 입력시 key error 발생

print((my_dict1['my_key'])) # key error가 발생하지 않음.
print((my_dict2['my_key']))
print((my_dict3['my_key']))
print((my_dict4['my_key']))

print(my_dict1)
print(my_dict2)
print(my_dict3)
print(my_dict4)

# 활용하기
my_dict1['my_key'] += 1
print(my_dict1)
print(my_dict1['my_key'])
my_dict3['my_key'].append(1)
print(my_dict3)
print(my_dict3['my_key'])