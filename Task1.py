# Задача 1

class Date:
    def __init__(self, da, moun, year):
        self.da=da
        self.moun=moun
        self.year=year
        print(self.da,self.moun,self.year)
    @classmethod
    def dmy(cls, st):
        st2=st.split('-')
        #print(st2)
        d,m,y=map(int,st2)
        return cls(d,m,y)

    @staticmethod
    def validaciya(inf):
        inf2=inf.split('-')
        inf2[0]= int(inf2[0])
        inf2[1]=int(inf2[1])
        inf2[2]=int(inf2[2])
        print(inf2[0], inf2[1],inf2[2])

        if inf2[0] <=0 or inf2[0]> 31:
            print( f"Неверно указана дата '{inf2[0]}'. Введите дату от 1 до 31")
        if inf2[1] <=0 or inf2[1] > 12:
            print( f"Неверно указан месяц '{inf2[1]}'. Введите месяц от 1 до 12")
        if inf2[2] <=0:
            print( f"Неверно указан год '{inf2[2]}'. Введите год более 0")
        elif 0<inf2[0]<31 and 0<inf2[1]<12 and inf2[2]>0:
            print(f"Дата введена в верном формате")


date=Date.dmy("12-04-2022")
print(type(date.da),type (date.moun), type (date.year))
Date.validaciya("41-16-0")
Date.validaciya('12-01-2022')