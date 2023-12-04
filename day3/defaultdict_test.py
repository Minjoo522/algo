from collections import defaultdict

my_dict1 = defaultdict(int)
my_dict2 = defaultdict(str)
my_dict3 = defaultdict(list)
my_dict4 = defaultdict(set)

print(my_dict1)
print(my_dict2)
print(my_dict3)
print(my_dict4)
# defaultdict(<class 'int'>, {})
# defaultdict(<class 'str'>, {})
# defaultdict(<class 'list'>, {})
# defaultdict(<class 'set'>, {})

# 없는 key로 검색해도 기본값을 만들어서 생성해줌
print(my_dict1['my_key'])  # 0
print(my_dict2['my_key'])
print(my_dict3['my_key'])  # []
print(my_dict4['my_key'])  # set()
print(my_dict1)  # defaultdict(<class 'int'>, {'my_key': 0})
print(my_dict2)  # defaultdict(<class 'str'>, {'my_key': ''})
print(my_dict3)  # defaultdict(<class 'list'>, {'my_key': []})
print(my_dict4)  # defaultdict(<class 'set'>, {'my_key': set()})

# 활용
my_dict5 = defaultdict(int)
my_dict5['my_key'] += 1
print(my_dict5)  # defaultdict(<class 'int'>, {'my_key': 1})
print(my_dict5['my_key'])  # 1