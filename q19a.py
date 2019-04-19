# ---------Simple Calculator


def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def sub(*args):
    subtraction = args[0]
    for i in args:
        if i == args[0]:
            continue
        else:
            subtraction -= i
    return subtraction


def Multiply(*args):
    mul = 1
    for i in args:
        mul *= i
    return mul


def Divide(*args):
    res = args[0]
    for i in args:
        if i == args[0]:
            continue
        else:
            if i == 0:
                return "Error Cannot Divide by Zero , Try Again"
            res //= i
    return res


myChoice = True
while(myChoice != '5'):
    print('''
        *************MENU*************
        1.Add
        2.Subtract
        3.Multiply
        4.Divide
        5.Exit
        ''')
    myChoice = input("Enter a choice: ")
    if myChoice == '1':
        myNumber = input("Enter list of numbers to add : ").split(',')
        myNumber = list(map(int, myNumber))
        print("Addition => {}".format(add(*myNumber)))

    elif myChoice == '2':
        myNumber = input("Enter list of numbers to Subtract : ").split(',')
        myNumber = list(map(int, myNumber))
        print("Subtraction => {}".format(sub(*myNumber)))

    elif myChoice == '3':
        myNumber = input("Enter list of numbers to Multiply : ").split(',')
        myNumber = list(map(int, myNumber))
        print("Multiplication => {}".format(Multiply(*myNumber)))

    elif myChoice == '4':
        myNumber = input("Enter list of numbers to Divide : ").split(',')
        myNumber = list(map(int, myNumber))
        print("Division => {}".format(Divide(*myNumber)))