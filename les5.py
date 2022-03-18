# Задача 1

with open ("text.txt", 'w', encoding="utf-8") as f:
    while True:
        a=input("Введите данные или нажмите ENTER для завершения : ")
        if a== "":
            break
        else:
            print(a, file=f)

# Задача 2

with open("Task2",'r', encoding="utf-8") as f2:
    st=0
    for i in f2:
        st+=1
        i2=i.split()
        w=0
        for el in i2:
            w+=1

        print (f'Количество слов в {st} строке: {i} равно: {w}')
    print(f"количество строк в файле: {st}")

# Задача 3

with open("Task3", 'r', encoding="utf-8") as f3:
    print("Оклад менее 20000 рублей имеют сотрудники:")
    su=0
    st=0
    for i in f3:
        i3= i.split()
        oklad= float(i3[1])
        su+=oklad
        st+=1
        if oklad < 20000:
            print (i3[0])
    sr=su/st
    print("Средняя величина дохода сотрудников равна: ", sr)

# Задача 4

di={'One': 'Один', "Two": 'Два', "Three": 'Три', 'Four': 'Четыре'}

with open("Task4", 'r', encoding="utf-8") as f4:
    with open('Task4-2','w', encoding="utf-8") as f4_2:
        for i in f4:
            i2= i.split()
            print(di[i2[0]],i2[1],i2[2], file= f4_2)

# Задача 5

with open("Task5.txt", 'w', encoding='utf-8') as f5:
    f5.writelines(input('Введите числа через пробел: '))
with open('Task5.txt','r', encoding='utf-8') as f5_2:
    s=0
    for i in f5_2:
        i2=i.split()
        for el in i2:
            el=int(el)
            s+=el
        print('Сумма чисел равна:', s )

# Задача 6

with open("Task6",'r', encoding='utf-8') as f6:
    di6={}
    for i in f6:
        i2=i.split()
        s=0
        for el in i2[1:]:
            el2=el.split('(')
            if el2[0] != '—':
                h= int(el2[0])
                s+=h
        di6[i2[0]]=s
    print(di6)

# Задача 7

with open('Task7','r', encoding='utf-8') as f7:
    opr=0 # общая прибыль неубыточных фирм
    n=0
    di7={}
    disr={}
    for i in f7:
        i2=i.split()
        vir= int(i2[2])
        izd=int(i2[3])
        prib=vir-izd
        #print(f'Прибыль фирмы {i2[0]} составляет: {prib}')
        di7[i2[0]]=prib
        if prib>0:
            opr+=prib
            n+=1
    srpr=opr/n
    disr['average_profit']= srpr
    #print('Средняя прибыль: ', srpr)
    li7=[di7,disr]
    print(li7)

import json
with open('Task7_2.json','w', encoding= 'utf-8') as f7_2:
    json.dump(li7,f7_2, ensure_ascii=False)