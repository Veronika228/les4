my_list = [1, 2, 2, 7, 4, 4, 5, 9, 7, 10, 12]
print(my_list)
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)