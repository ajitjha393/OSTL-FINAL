class X(object):
    def __init__(self):
        print('Constructor of class X called ....')
        super().__init__()

class Y(object):
    def __init__(self):
        print('Constructor of class Y called ....')
        super().__init__()

class Z(object):
    def __init__(self):
        print('Constructor of class Z called ....')
        super().__init__()
class A(X,Y):
    def __init__(self):
        print('Constructor of class A called ....')
        super().__init__()
class B(Y,Z):
    def __init__(self):
        print('Constructor of class B called ....')
        super().__init__()

class M(A,B,Z): #--Edited this missed Class Z to extend,(credit ---> Farhan)
    def __init__(self):
        print('Constructor of class M called ....')
        super().__init__()

obj = M()
