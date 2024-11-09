my_dict ={'Grisha':2002, 'Petr':2004}
print(my_dict)
print(my_dict['Grisha'])
print(my_dict.get('Kolya', 'Такого значения здесь нет'))
my_dict['Anton'] = 2001
my_dict['Den'] = 1979
print(my_dict)
del my_dict['Anton']
print(my_dict)
my_set = {1,3,4,75.3}
print(my_set)
my_set.update([345, 'John'])
my_set.remove(3)
print(my_set)