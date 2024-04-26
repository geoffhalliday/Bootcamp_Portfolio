# User inputs number of students registering for an exam (stored in variable 'num_students')
# Then a For loop is used to allow the user to enter each student ID ('id_number')
# A dotted line is added to the student ID to allow a signature when printed
# This is all written to file 'reg_form.txt'

with open("reg_form.txt", "w") as file:
    num_students = int (input ("How many students are registering? "))
    for x in range (num_students):
        id_number = input ("Enter next ID number: ")
        file.write (id_number + "  ..............................\n")
        
        


