def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(a=2, b=5)
print_params(b=25)
print_params(c=[1,2,3])


values_list = [5,'новая', False]
values_dict = {'a' : 10, 'b' : True, 'c' : 'Hi'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.35,'Строка']
print(*values_list_2,42)