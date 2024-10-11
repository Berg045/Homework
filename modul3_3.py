def print_params(a = 1, b = 'строка', c = True):

    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

def print_params(param1, param2, param3):
    print(param1, param2, param3)

values_list = [11, "Формула", 3.14]
values_dict = {'param1': True,'param2': None,'param3': [1, 2, 3]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)