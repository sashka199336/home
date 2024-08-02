a= int(input('Введи первое число'))
b= int(input('Введи второе число'))
c= int(input('Введи третье число'))
if a==b==c:
print("3")
elif a!=b and b!=c and c!=a:
print(0)
elif a!=b or b!=c or c!=a:
print(2)
