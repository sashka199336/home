my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

while True:
a=int(input("Введите число из списка 'my_list'"))
if a==0:
continue
if a<=0:
break
if a == 42 or a == 69 or a == 322 or a == 13 or a==99:
print(a)
continue
if a == 9 or 8 or 5:
break
