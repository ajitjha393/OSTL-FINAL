def increaseResultBy4(myFunction):
    def wrapperFunction(*args, **kwargs):
        return myFunction(*args, **kwargs) + 4
    return wrapperFunction



@increaseResultBy4
def findSquare(num):
    return num ** 2


@increaseResultBy4
def findCube(num):
    return num ** 3


print(
    'Square of number increased by 4 => {}'.format(findSquare(int(input("Enter a number to find square : ")))))

print(
    'Cube of a number multiply by 4 => {}'.format(findCube(int(input("Enter a number to find Cube : ")))))