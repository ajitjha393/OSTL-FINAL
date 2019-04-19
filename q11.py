# for storing object in file we use serilization(pickle)

import pickle

class Patient(object):
    no_of_patient = 0

    def __init__(self,pid,name,ward_no,age):
        self.pid = pid
        self.name = name
        self.ward_no = ward_no
        self.age = age

    def set_details(self,gender,blood_group):
        self.gender = gender
        self.blood_group = blood_group

    def display_details(self):
        #-----C style format for printing ------#
        #-----Makes it more cleaner and cooler----#
        if self.gender == 'M':
            print('%-10s %-10s %-10s %-10s %-10s %-10s'%(self.name,self.pid,self.ward_no,self.age,self.gender,self.blood_group))
     
    @classmethod

    def set_no_of_patient(cls):
        cls.no_of_patient += 1



def Insert_patient():
    patient_list = open('patients.bin','ab')
    name,pid,ward_no,age,gender,blood_group = input('Enter the name,pid,ward_no,age,gender,blood_group of Patient : ').split(',')
    patient_obj = Patient(pid,name,ward_no,age)
    patient_obj.set_details(gender,blood_group)
    Patient.set_no_of_patient()
    pickle.dump(patient_obj,patient_list)
    patient_list.close()

def Read_Back_details():
    patient_list = open('patients.bin','rb') 
    for i in range(Patient.no_of_patient):
        pickle.load(patient_list).display_details()
    patient_list.close()

Insert_patient()
Insert_patient()
Insert_patient()
Insert_patient()
Read_Back_details()    

