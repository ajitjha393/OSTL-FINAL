#----Queue Follows FIFO , insertion at end,Deletion at beg------#
class Queue(object):
    def __init__(self):
        self.queue = []

    def Enqueue(self,value):
        self.queue.append(value)
        

    def Dequeue(self):
        return self.queue.pop(0)

    def Display_Queue(self):
        for i in self.queue:
            print(i,end = " ")
        print('front = {} rear = {}'.format(self.queue[0],self.queue[-1]))    

    def Search(self,value):
        return self.queue.index(value)                  

#-------MENU DRIVEN REFER TO Q1------------#

myQueue = Queue()

myQueue.Enqueue(30)
myQueue.Enqueue(40)
myQueue.Enqueue(50)
myQueue.Enqueue(60)
myQueue.Enqueue(70)

myQueue.Display_Queue()

myQueue.Dequeue()
myQueue.Dequeue()

myQueue.Display_Queue()


print('60 is present at index = ',myQueue.Search(60))