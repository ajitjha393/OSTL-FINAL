from functools import reduce

#---Create a file---#
myFile = open('foo.txt','w')
myText = ''

# This small maneuver i have done for taking multi line input
# Here if the user enters -1 we will come out of loop of taking entry
print('Enter -1 to save the content to the file')
print('Enter the contents of the file : ')
while True :
    x = input()
    if x == '-1':
        break
    else :
        myFile.write(x + '\n')

myFile.close()

#----Open the file for reading -----#
myFile = open('foo.txt','r')

my_file_content = myFile.read()
#--Since there are multiple lines,We separate each line by splitting over newline
my_file_content = my_file_content.split('\n') 


 #--Num of lines is calculated by finding length of list ---#
numOfLines = len(my_file_content) - 1  #--- -1 because last character is \n----#


#For finding number of words,First i join all the lines separated by space using ' '.join(list to be join) 
# Then on that i use split(' ') ,what this will do is it will separate all words by space
# and form a list whose length will give number of words


numOfWords = len(' '.join(my_file_content).split(' ')) - 1


#---For finding number of char add len of all the words......
#---Lambda will reduce hardwork for u ,but if not comfortable with lamda 
# use this----- and comment the lambda one..

#numOfChar = 0
#for i in my_file_content:
#   numofChar += len(i)   



numOfChar = reduce(
    lambda x, y: x+y, list(map(lambda x: len(x), my_file_content)))

print('No of lines = > {} \n No of  Words = {} \n No of Char = {}'.format(
    numOfLines, numOfWords, numOfChar))


#----For finding longest word search in the list and find max length-----#


i = -1
for word in ' '.join(my_file_content).split(' '):
    if i < len(word):
        i = len(word)
        longest_word = word
    
print('Longest Word in the file => ',longest_word)

content_of_old_file = myFile.read()
myFile.close() #---Close prev file---#



#-----Create a new file------#
my_new_File = open('foo2.txt','w')
my_new_File.write(content_of_old_file)


