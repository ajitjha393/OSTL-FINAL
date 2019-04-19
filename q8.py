#----WHAT IS DUCK TYPING ------#
'''
We know that in python ,content of variable is decided during running time 
So it is possible to call a method or attribute which may not be belonging to its own class
leading to run time error ,unlike java where we declare reference before itself
eg.... 
class_name abc = new class_name()
so here we know abc is obj of type class_name


Duck typing in python is an application of the duck test—
"If it walks like a duck and it quacks like a duck, then it must be a duck"—
to determine if an object can be used for a particular purpose.
 With normal typing, suitability is determined by an object's type.
In duck typing, an object's
suitability is determined by the presence of certain methods and properties, rather than the type of the object itself.

Ref -> https://en.wikipedia.org/wiki/Duck_typing
'''

class Duck:
    def fly(self):
        print("Duck flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

class Whale:
    def swim(self):
        print("Whale swimming")

def fly(entity):
    try:
        entity.fly()

    except AttributeError as ae:
        print(ae)

duck = Duck()
airplane = Airplane()
whale = Whale()

fly(duck) # prints `Duck flying`
fly(airplane) # prints `Airplane flying`
fly(whale) # Throws the error `'Whale' object has no attribute 'fly'` Hence we handle it using try except

