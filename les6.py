# Задача 1

import time
class TrafficLight:
    def __init__(self, color):
        self.__color= color

    def running(self):
        i=1
        while True:
            print(self.__color[0])
            time.sleep(7)
            print(self.__color[1])
            time.sleep(2)
            print(self.__color[2])
            time.sleep(3)
            i+=1
            if i>3:
                break

TL= TrafficLight(['Красный', "Жёлтый", "Зелёный"])
TL.running()

# Задача 2

class Road:
    def __init__(self, length, width):
        self._l= length
        self._w= width

    def method(self):
        d=int (input("Введите толщину дорожного полотна в см: "))
        # масса асфальта для покрытия одного кв. метра дороги асфальтом,
        # толщиной в 1 см= 25 кг из примера
        weigh=self._l *self._w*25*(d/100)
        print(f'Масса асфальта для покрытия всей дороги равна: {weigh} кг')

road1= Road(200, 5)
road1.method()

# Задача 3

class Worker:
    def __init__(self, name, surname, position, income):
        self.name= name
        self.surname= surname
        self.position= position
        self._income= income

class Position(Worker):
    def get_full_name(self):
        print(self.name ,self.surname)

    def get_total_income(self):
        total= self._income["wage"]+self._income['bonus']
        print(f'Доход сотрудника составляет {total}')


person1= Position("Иван", "Сидоров", "врач", {"wage": 5000, "bonus": 500})
person1.get_full_name()
print(person1.position)
person1.get_total_income()

person2=Position("Пётр", "Иванов", "врач-реаниматолог", {"wage": 7000, "bonus": 250})
person2.get_full_name()
print(person2.position)
person2.get_total_income()

# Задача 4

class Car:
    def __init__(self,speed, color, name, is_police):
        self.speed= speed
        self.color=color
        self.name=name
        self.police= is_police

    def go(self):
        print("Машина поехала")
    def  stop(self):
        print("Машина остановилась")
    def turn_left(self):
        print("Машина повернула налево")
    def turn_right(self):
        print('Машина повернула направо')
    def show_speed(self):
        print(f"Текущая скорость автомобиля составляет: {self.speed} км/ч")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, pas):
        Car.__init__(self,speed, color, name, is_police)
        self.pas=pas
    def show_speed(self):
        if self.speed>60:
            print("Превышение скорости!")
        else:
            print(f"Текущая скорость автомобиля составляет: {self.speed} км/ч")

class SportCar(Car):
    def sport(self):
        print("Машина разгоняется до 220 км/ч")
class WorkCar(Car):
    def show_speed(self):
        if self.speed>40:
            print("Превышение скорости!")
        else:
            print(f"Текущая скорость автомобиля составляет: {self.speed} км/ч")
class PoliceCar(Car):
    def police1 (self):
        print("Машина используется только сотрудниками полиции")

towncar=TownCar(70, 'зелёный', "Mazda", 'нет',5)
sportcar=SportCar (200, "красный", "Opel", 'нет')
workcar=WorkCar(35, "жёлтый", "Reno", 'нет')
policecar=PoliceCar(90, 'белый', 'Nissan', 'да')

print(f'Скорость составляет: {towncar.speed} км/ч')
print(f'Количество мест: {towncar.pas}')
towncar.show_speed()
towncar.turn_left()

print()
sportcar.sport()
sportcar.show_speed()
sportcar.go()
print(f"Цвет машины: {sportcar.color}")

print()
print(f"Название машины: {workcar.name}")
workcar.show_speed()
workcar.stop()

print()
policecar.police1()
policecar.turn_right()
print(f"Машина {policecar.name}, цвeт: {policecar.color}, является полицией: {policecar.police}")

# Задача 5

class Stationery:
    def __init__(self, title):
        self.title=title
    def draw(self):
        print('Запуск отрисовки')

class Pen (Stationery):
    def draw(self):
        print('Ручка имеет тонкий стержень')

class Pencil(Stationery):
    def draw(self):
        print('Карандаш можно легко стереть')

class Handle(Stationery):
    def draw(self):
        print('Маркет пишет синим цветом')

stationery=Stationery("Чернильная ручка")
stationery.draw()

pen=Pen("ABC")
pen.draw()

pencil= Pencil("KN")
pencil.draw()

handle= Handle("Цветные маркеры")
handle.draw()