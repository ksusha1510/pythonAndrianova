# Задача 7

class Compl:
    def __init__(self,n):
        self.n=n

    def __add__(self, other):

        new= int(self.n.split('+')[0])+ int(other.n.split('+')[0]), int (self.n.split('+')[1].split('*')[0])+int (other.n.split('+')[1].split('*')[0])
        return f'{new[0]}+{new[1]}*i'

    def __mul__(self, other):
        # (a+bi)(c+di)= (ac-bd)+(ad+bc)*i
        ac=int(self.n.split('+')[0])*int(other.n.split('+')[0])
        bd=int (self.n.split('+')[1].split('*')[0])*int (other.n.split('+')[1].split('*')[0])
        ad= int(self.n.split('+')[0])*int (other.n.split('+')[1].split('*')[0])
        bc= int (self.n.split('+')[1].split('*')[0])*int(other.n.split('+')[0])
        z= ac-bd
        k=ad+bc
        return f'{z}+{k}*i'

num1=Compl("5+4*i")
num2=Compl('-2+3*i')

print(num1+num2)
print(num1*num2)

