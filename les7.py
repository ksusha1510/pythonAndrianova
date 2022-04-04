# Задача 1

class Matrix:
    def __init__(self, list):
        self.list= list

    def __str__(self):
        for i in range (len(self.list)):
            for j in range (len(self.list[i])):
                print("  |  ", self.list[i][j], end='')
            print('  |')
        return ''

    def __add__(self, other):
        for i in range (len(self.list)):
            for j in range (len(self.list[i])):
                new= self.list[i][j]+other.list[i][j]
                print("  |  ", new, end='')
            print('  |')
        return ''

matrix1=Matrix([[1,2, 8],[3,4, 9],[5,6, 10], [11, 12, 13]])
print(matrix1)
print()
matrix2=Matrix([[9,8,7],[6,5,4],[3,2,1],[10,11,12]])
print(matrix2)
print()
print(matrix1+matrix2)

# Задача 2

from abc import ABC, abstractmethod

class Clothes (ABC):
    @abstractmethod
    def rashod(self):
        print('')
class Coat(Clothes):
    def __init__(self, V):
        self.V=V

    @property
    def V (self):
        return self__V

    @V.setter
    def V (self,V):
        if V < 40:
            self.__V = 40
        elif V > 56:
            self.__V = 56
        else:
            self.__V = V

    def info_coat(self):
        print(f"Размер пальто: {self.__V}")

    def rashod(self):
        r_coat= self.__V/6.5 + 0.5
        print(f"Расход ткани для пальто составляет: {round (r_coat, 2)} м")
        return r_coat


class Costume (Clothes):

    def __init__(self, H):
        self.H = H

    @property
    def H (self):
        return self.__H

    @ H.setter
    def H (self, H):
        if H<150:
            self.__H=150
        elif H>190:
            self.__H=190
        else:
            self.__H=H

    def info(self):
        print(f"Рост костюма: {self.__H}")


    def rashod(self):
        r_costume= 2*self.__H + 0.3
        print(f"Расход ткани для костюма составляет: {round(r_costume,2)} м")
        return r_costume

coat= Coat(int(input("Введите размер пальто: ")))
#coat.rashod()
costume=Costume(int(input("Введите роcт костюма: ")))
#ostume.rashod()

coat.info_coat()
costume.info()
sum= coat.rashod()+costume.rashod()
print(f'Общий расход ткани составляет {round(sum,2)} м')


# Задача 3

class Cell:
    def __init__(self, n):
        self.n=n

    def __add__(self, other):
        return Cell (self.n+other.n)
    def __sub__(self, other):
        if self.n-other.n >0:
            return  Cell (self.n-other.n)
        else:
            print("Операция невозможна: разность ячеек меньше нуля")
    def __mul__(self, other):
        return Cell(self.n * other.n)
    def __truediv__(self, other):
        return Cell(self.n // other.n)
    def __str__(self):
        return f'Клетка имеет {self.n} ячеек'

    def make_order(self, obj, a):

        print ((('*'* a)+ '\n') * (self.n//a), '*'*(self.n%a))

cell1=Cell(int(input("Введите количество ячеек в клетке cell1: ")))
cell2=Cell(int(input("Введите количество ячеек в клетке cell2: ")))
print(cell1+cell2)
print(cell2-cell1)
print(cell1-cell2)
print(cell1*cell2)
print(cell1/cell2)
cell1.make_order(cell1.n, 5)