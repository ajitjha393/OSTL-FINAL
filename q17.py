from functools import reduce

#---Create a file---#
myFile = open('foo.txt','w')
myText = ''

# This small maneuver i have done for taking multi line input

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
my_file_content = my_file_content.split('\n')


numOfLines = len(my_file_content) - 1
numOfWords = len(' '.join(my_file_content).split(' ')) - 1
numOfChar = reduce(
    lambda x, y: x+y, list(map(lambda x: len(x), my_file_content)))

print('No of lines = > {} \n No of  Words = {} \n No of Char = {}'.format(
    numOfLines, numOfWords, numOfChar))

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


