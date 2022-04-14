# Задача 4-6

# Организация работы неврологического отделения

class Person():
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname
    def __str__(self):
        return f'Фамилия и имя: {self.surname} {self.name}'

class Patient(Person):
    def __init__(self, name, surname, age, sex, complaint):
        Person.__init__(self, name, surname)
        self.comlaint=complaint
        self.age=age
        self.sex=sex
        self.osmotr=[]
        self.obsled=[]
        self.lecenie=[]
        self.diagnoz=[]

    def osm(self, doct):
        self.osmotr.append(doct)
        #print (self.osmotr)

    def obs(self, metod):
        self.obsled.append(metod)
    def lecen(self,lec):
        self.lecenie.append(lec)
    def dia(self,diagn):
        self.diagnoz.append(diagn)
    def epicriz(self):
        print(f'Пациент {self.surname} {self.name} {self.sex} {self.age} поступил в неврологическое отделение с жалобами на {self.comlaint}. За время лечения был осмотрен: {self.osmotr}. Проведено обследование: {self.obsled}. Выставлен диагноз: {self.diagnoz}. Проведено лечение: {self.lecenie}. Выписан с положительной динамикой')

class Staff(Person):
    def work(self):
        print("Оказание медицинской помощи пациентам")
class Doctor(Staff):
    def exam(self, pat):
        pat.osm({"врач": self.surname + " "+ self.name})
    def nazn_obsl(self,pat):
        met=input("Введите методы обследования (напр ОАК, УЗИ, МРТ): ")
        pat.obs(met)
    def nazn_lec(self,pat,nur, lec):
        nur.vipolnenie_naznaceniy (pat, lec)
    def ust_diag(self,pat,diag):
        pat.dia(diag)

class Neurologist(Doctor):
    def exam(self, pat):
        pat.osm( {"невролог": self.surname + " "+ self.name})
class Zav(Doctor):
    def exam(self, pat):
        pat.osm({"зав. отделения": self.surname + " "+ self.name})
class Prof(Doctor):
    def exam(self, pat):
        pat.osm( {"проф. каф. неврологии и нейрохирургии": self.surname + " "+ self.name})

class Nurse(Staff):
       def vipolnenie_naznaceniy(self,pat,lec):
        pat.lecen(lec)


class Diagnosis():
    def __init__(self, *diag):
        self.diag= list (diag)

    def my_diag(self):
        return self.diag

class Drug():
    def __init__(self, *drug_name):
        self.drug_name=drug_name

p1=Patient("Иван", "Иванов", 66, "м", "боль в ПОП")
n1=Neurologist("Пётр", " Петров")
prof=Prof("Владимир Михайлович", "Бехтерев")
zav=Zav("Екатерина Михайловна", "Сидорова")
ms=Nurse('Елена', "Белова")
d=Drug({'диклофенак': "в/м"}, {"мадопар": "внутрь"}, {"эмоксипин":"в/в"}, {'интерферон бета':"п/к"})
di=Diagnosis("Дискогенная радикулопатия", "Болезнь Паркинсона", "Рассеянный склероз", "Эпилепсия")
print(p1)
zav.exam(p1)
n1.exam(p1)
prof.exam(p1)
#print(p1.osmotr)
n1.nazn_obsl(p1)
#print(p1.obsled)

n1.nazn_lec(p1,ms, d.drug_name[0])
#print(p1.lecenie)
zav.ust_diag(p1,di.diag[0])
#print(p1.diagnoz)

p1.epicriz()