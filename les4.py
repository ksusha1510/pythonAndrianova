# Задача 1

# Введите через пробел выработку в часах, ставку в час и премию

from sys import argv
v, s, p = map(int, argv[1:])

def zar():
    zp= v*s + p
    print("Заработная плата сотрудника: ", zp)
    return zp
zar()

# Задача 2

li1= [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

li2= [li1[(i+1)] for i in range (len(li1)-1) if li1[(i+1)]>li1[i]]

print (li1)
print (li2)

# Задача 2 c вводом чисел

li1= input("Введите числа через пробел: ").split()
l3= [int(el) for el in li1]
li2= [l3[i+1] for i in range (len(l3)-1) if l3[i+1]>l3[i]]

print (li1)
print (li2)

# Задача 3

l1= [i for i in range(20, 240) if i%20==0 or i%21==0]
print(l1)

# Задача 4

li4= input("Введите числа через пробел: ").split()
li4= [int(el) for el in li4]

new=[el for el in li4 if li4.count(el)==1]

print (new)

# Задача 5

from functools import reduce
li5=[i for i in range (100, 1001) if i%2==0]
print (li5)

def my_fun(a,b):
    return a*b

print(reduce (my_fun, li5))

# Задача 6

from itertools import count, cycle

n= int (input("Введите число меньше 20: "))
for el in count (n):
    if el > 20:
        break
    print (el)

li6=input("Введите элементы списка: ").split()
i=0
for el2 in cycle (li6):
    print(el2)
    i+=1
    if i>15:
        break

# Задача 7

n=int(input("Введите число: "))

def my_fact():
    fact= (i for i in range(1,n+1))
    f=1
    if n==0:
        f=1
        print (n, "!=", f)
    else:
        for el in fact:
            f*=el
            print(el, "!=", f)
            yield f



res=my_fact()
for elem in res:
    print()