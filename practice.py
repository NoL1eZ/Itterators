

list_of_lists_2 = [[['a'], ['b', 'c']], ['d', 'e', [['f'], 'h'], False], [1, 2, None, [[[[['!']]]]], []]]
list_of_list1 = sum(list_of_lists_2, [])
list_of_list = sum(list_of_list1, [])
print(type(list_of_list))