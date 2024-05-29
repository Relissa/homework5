immutable_var = 1, 2, 'home', True
print(immutable_var)
#immutable_var[0] = 3
#'tuple' object does not support item assignment - не поддерживает обращение по элементам
mutable_list = [1, 2, 'home', True]
mutable_list[0] = 7
mutable_list[1] = 8
mutable_list[2] = 'work'
mutable_list[3] = False
print(mutable_list)
