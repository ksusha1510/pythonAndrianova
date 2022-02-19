# Задача 1

li= [5, 11.2, "6", "зима", True, [1,2,9], (10, "дождь"), {"лето": "summer"} ]
print (li)
for el in li:
    print (el, type(el))

print ()
# Задача 2

l1= input ("Введите элементы списка через пробел: ").split()
print (l1)
for i in range (0, len(l1)-1,2):
    l1 [i], l1 [i+1] = l1 [i+1], l1 [i]

print (l1)

print()
# Задача 3 через словарь

mon= int (input ("Введите месяц в виде числа от 1 до 12: "))
year ={"зима": [1,2,12],"весна": [3,4,5], "лето": [6,7,8], "осень": [9,10,11]}
if mon >=1 and mon<=12:
    for el in year:
        if mon in year[el]:
            print (el)
else:
    print ('Введено неверное значение месяца')

# Задача 3 через список

mon= int (input ("Введите месяц в виде числа от 1 до 12: "))
win=[1,2,12]
sp=[3,4,5]
sum= [6,7,8]
aut= [9,10,11]
year= [win,sp,sum,aut]
seas=["зима","весна","лето","осень"]
if mon >=1 and mon<=12:
    for i in range (0,len(year)):
        if mon in year [i]:
           print (seas [i])
else:
    print ('Введено неверное значение месяца')


print()
# Задача 4

st= input ("Введите элементы строки через пробел: ").split()

for i in range (0, len(st)):
    n= i+1
    print (n, st[i][0:10])

print()
# Задача 5

my_list= [7,5,3,3,2]

while True:
    n= input ("Введите новый элемент рейтинга или для завершения работы введите stop:")
    if n.lower()== 'stop':
        break
    else:
        n= int (n)
        for i in range (0, len (my_list)):
            if n> my_list[i]:
                my_list.insert (i,n)
                break
            elif n==my_list [i]:
                my_list.insert (i+1,n)
                break
        else:
            my_list.append (n)
    print (my_list)
print("Рейтинг:", my_list)
