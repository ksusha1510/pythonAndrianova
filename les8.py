# Задача 2

class Zero(Exception):
    def __init__(self, txt):
        self.txt=txt

try:
    a = int(input("Введите делимое число: "))
    b = int(input("Введите делитель : "))
    if b==0:
        raise Zero ("Деление на 0 невозможно")
except ValueError:
    print("Введено не число")
except Zero as err:
    print(err)
else:
    print(f'a/b= {a/b}')

print()

# Задача 3

class Number(Exception):
    def __init__(self, txt):
        self.txt=txt
li2=[]
def f1():
    while True:
        li = input("Введите элементы списка или введите stop для завершения: ").split()
        for el in li:
            if el == 'stop':
                return
            else:
                try:
                    el = int(el)

                    if type(el)==int or float:
                        li2.append(el)
                    else:
                        raise Number ("Вводите только числа")
                except (Number, ValueError) as err:
                    print('Вводите числа')
        print(li2)
f1()
print(li2)