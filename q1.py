class LinkedList(object):
    def __init__(self):
        self.linkedlist = []

    def display_list(self):
        for node in self.linkedlist:
            print(node,end = " --> ")   
        print("Null")      

    def Insert_at_beg(self,value):  
        self.linkedlist.insert(0,value)
        

    def  Insert_at_end(self,value):
        self.linkedlist.append(value)

    def Insert_at(self,index,value):
        self.linkedlist.insert(index,value)

    def Delete_from_beg(self):
        self.linkedlist.pop(0)

    def Delete_from_end(self):
        self.linkedlist.pop()

    def Delete_at(self,index):
        self.linkedlist.pop(index)

    def Delete_element(self,element):
        self.linkedlist.remove(element) 

    def Search(self,element):
        return self.linkedlist.index(element) 

    def Replace(self,index,value):
        self.linkedlist[index] = value

    def Forward_Traversal(self):
        self.display_list()                                 

    def Reverse_Traversal(self):
        print("Null",end = " --> ")    
        for node in self.linkedlist[::-1] :
            print(node,end = " --> ")   
           

    def Insert_after_element(self,prevElement,newElement):
        self.linkedlist.insert(self.linkedlist.index(prevElement)+1,newElement)    



#-------MENU DRIVEN--------#
#----For all menu driven Do same thing -----#
myLinkedList = LinkedList()
    
while(True):
    print('''
        1. Display List
        2. Insert at beg
        3. Insert at end
        4. Insert at specified position
        5. Delete from beg
        6. Delete from end
        7. Delete from specified position
        8. Delete a particular element
        9. Search an element
        10. Replace element at specified index
        11. Forward Traversal
        12. Reverse Traversal
        13. Insert after an element
        14. Exit
    --------------------------------------------------- 
        ''')
    choice = int(input('Enter a choice : '))

    if(choice == 1):
        myLinkedList.display_list()

    elif(choice == 2):
        myLinkedList.Insert_at_beg(int(input('Enter value to be inserted : ')))

    elif(choice == 3):
        myLinkedList.Insert_at_end(int(input('Enter value to be inserted : ')))            
    
    elif(choice == 4):
        myLinkedList.Insert_at(int(input('Enter index : ')),int(input('Enter value to be inserted : ')))
                   
    elif(choice == 5):
        myLinkedList.Delete_from_beg()

    elif(choice == 6):
        myLinkedList.Delete_from_end()

    elif(choice == 7):
        myLinkedList.Delete_at(int(input('Enter the index : ')))

    elif(choice == 8):
        myLinkedList.Delete_element(int(input('Enter element to be deleted : ')))

    elif(choice == 9):
        print('Element present at index : ',myLinkedList.Search(int(input('Enter the element to be searched : '))))

    elif(choice == 10):
        myLinkedList.Replace(int(input('Enter the index : ')),int(input('Enter the new element : ')))            
    elif(choice == 11):
        myLinkedList.Forward_Traversal()

    elif(choice == 12):
        myLinkedList.Reverse_Traversal()
    elif(choice == 13):
        myLinkedList.Insert_after_element(int(input('Enter the element after which value is to be inserted : ')),int(input('Enter the new value : ')))            
    elif(choice == 14):
        break        