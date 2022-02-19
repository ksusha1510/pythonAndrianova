#Задача 6

tovar= []
i=1
while True:
    stop= input ("Для завершения ввода данных введите stop, для продолжения нажмите клавишу enter")
    if stop.lower()=="stop":
        break
    else:
        naz= input("Введите наименование товара: ")
        cen= input("Цена товара: ")
        kol=input ("количество: ")
        ed=input ("единица измерения: ")
        di= {"Название": naz , "Цена": cen , "количество": kol , "единица измерения": ed}
        co= (i, di)
        i=i+1
        tovar.append (co)
for el in tovar:
    print (el)

di_analit={}
li_naz=[]
li_cen=[]
li_kol=[]
li_ed=[]
for n in range (0, len(tovar)):
    har=tovar[n][1]
    li_naz.append(har['Название'])
    li_cen.append(har['Цена'])
    li_kol.append(har['количество'])
    li_ed.append(har['единица измерения'])
di_naz={"Название":li_naz}

di_analit={"Название":li_naz, "Цена":li_cen, "количество":li_kol,"единица измерения":li_ed}
print()
print (di_analit)
print (di_analit.keys())

poisk= input("Введите, какая из предложенных выше характеристик вас интересует:")
print (di_analit[poisk])