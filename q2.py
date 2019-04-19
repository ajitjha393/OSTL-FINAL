class Stack(object):
    def __init__(self):
        self.Stack = []

    def Push_Element(self,value):
        self.Stack.append(value)

    def Pop_Element(self):
        if(len(self.Stack) != 0):
            return self.Stack.pop()
        return 'Error,Stack is empty '    

    def peek(self):
        return self.Stack[-1]

    def display_stack(self):
        print('Stack is : ')
        for i in self.Stack[::-1]:
            print(i)

    def Search(self,value):
        return self.Stack.index(value)                


#-----MENU DRIVEN SAME AS IN Q1------#

myStack = Stack()

myStack.Push_Element(25)
myStack.Push_Element(40)
myStack.Push_Element(30)


myStack.display_stack()
print('--------------------')

print('Element 30 is present at index = ',myStack.Search(30))

print('Element Popped = ',myStack.Pop_Element())
print('Element Popped = ',myStack.Pop_Element())

myStack.display_stack()
print('--------------------')

print('Top of stack = ',myStack.peek())





