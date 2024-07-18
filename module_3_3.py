def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params(b = 25), print_params(c = [1,2,3])

values_list=(4,'gulash',True)
values_dict={'a':9,'b':"Hohland", "c":False}
print_params(*values_list)
print_params(**values_dict)

values_list_2=(14,"guhat")
print_params(*values_list_2, 52)
