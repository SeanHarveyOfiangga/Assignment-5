#Program 1: PUP Grading System
#Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
#Create a program that will ask for grade percentage. 
#Display the equivalent Grade/Mark and Description
#Input grade: 87.6
#Grade/Mark: 1.75
#Description: Very Good

#Grade percentage
def Grade_percentage():
    Percentage = float(input("Enter your grade percentage here: "))
    # step 1 - 1.0 | Excellent 
    if Percentage >= 97 and Percentage <=100:
        print ("Grade/Mark: 1.0")
        print ("Description: Excellent")
    # step 2 - 1.25 | Excellent
    elif Percentage >= 94 and Percentage <=96:
        print ("Grade/Mark: 1.25")
        print ("Description: Excellent")
    else:
        print ("Others")
        
Equivalent = Grade_percentage()
