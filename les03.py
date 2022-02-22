# Задача 1

def my_fun ():
    a=int (input ("a="))
    b= int (input ("b="))
    try:
        res= a/b
        return res
    except ZeroDivisionError:
        return "Деление на 0 невозможно"

r= my_fun ()
print ("a/b=", r)


# Задача 1 c запросом чисел вне функции и аргументами внутри функции

a = int(input("a="))
b = int(input("b="))
def my_fun (a,b):
    try:
        res= a/b
        return res
    except ZeroDivisionError:
        return "Деление на 0 невозможно"

r2= my_fun (a,b)
print (r2)

print()
# Задача 2

def dan (name, surname, year, city, email, phone):

    print (f'name: {name}, surname: {surname},year: {year}, city:{city},email:{email}, phone:{phone}')

name = input("Имя: ")
surname = input("Фамилия: ")
year = input("Год рождения:")
city = input("Город проживания: ")
email = input("email: ")
phone = input("Телефон: ")

dan (name=name, surname=surname, year=year,city=city, email=email, phone=phone)


print()
# Задача 3

def my_fun (a,b,c):
    if a<=b and a<=c:
        res= b+c
    elif b<=a and b<=c:
        res= a+c
    else:
        res= a+b
    return res

a = int(input("a="))
b= int (input ("b="))
c = int(input("c="))

r= my_fun(a,b,c)
print ("Сумма наибольших чисел равна: ", r)
r2= my_fun(6,1,4)  # вариант с заданными значениями
print ("Сумма наибольших чисел равна: ",r2)

# Задача 4

х= int (input("Введите положительное число х: "))
y= int (input("Введите отрицательное число y: "))

def my_func (х, y):
    res= х**y
    return res
r=my_func(х,y)
print (r)

# Задача 4 вариант 2

x= int (input("Введите положительное число х: "))
y= int (input("Введите отрицательное число y: "))

def my_func (x, y):
    n=1
    a=1
    while n<=abs(y):
        a= 1/x * a
        n+=1
    return a

r=my_func(x,y)
print (r)

# Задача 5

def f1():
    s=0
    while True:
        st = input("Введите числа через пробел. Для завершения введите q: ").split()
        for el in st:
            if el == "q":
                print (s)
                return
            else:
                el = int(el)
                s= el+s
        print (s)
    return s

f1()

# Задача 6

def int_func():
    st1= input("Введите слово маленькими латинскими буквами: ")
    st2= st1.capitalize()
    print (st2)

int_func()

# Задача 7

def int_func2():
    st1= input("Введите слова маленькими латинскими буквами через пробел: ")
    st2= st1.title()
    print (st2)

int_func2()
