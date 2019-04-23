# \w means any charatcer or number upper and lower case
#{} specifies range of length of character eg... {1,4} all characters have length between 1 and 4


import re
my_file = open('Test.txt','w')

my_dummy_text =\
'''This project is assign to Mr. Nageshwaran
Rao at nageswaran.rao@abc.net , and in case 
of any queries , you can contact Mr. Mahesh
at mahesh.k@gmail.com or Ms. Veena Sharma 
at sveenal3@pqr.org , who would be assistant
project co-ordinators.
'''
#---Save text in the file---#
my_file.write(my_dummy_text)
my_file.close()

#----Open file for reading-----#
my_file = open('Test.txt','r')
email_list =re.findall("[\w]{1,10}[.\w]{1,5}@[\w]+\.[\w]{1,5}",my_file.read())
print(email_list) 
my_file.close()   