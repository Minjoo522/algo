my_dict = {'c': 5, 'a': 5, 'b': 3, 'e': 4, 'd': 3}
# print(sorted(my_dict))  # ['a', 'b', 'c', 'd', 'e']
print(sorted(my_dict.items()))  # [('a', 5), ('b', 3), ('c', 5), ('d', 3), ('e', 4)] ✅ key 값 순서로 정렬
print(sorted(my_dict.items(), key=lambda x: x[1]))
# [('b', 3), ('d', 3), ('e', 4), ('c', 5), ('a', 5)] ✅ value 값 순서로 정렬
print(sorted(my_dict.items(), key=lambda x: -x[1]))
# [('c', 5), ('a', 5), ('e', 4), ('b', 3), ('d', 3)]
print(sorted(my_dict.items(), key=lambda x: (-x[1], x[0])))
#  [('a', 5), ('c', 5), ('e', 4), ('b', 3), ('d', 3)]
