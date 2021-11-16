#Program 1: PUP Grading System
#Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
#Create a program that will ask for grade percentage. 
#Display the equivalent Grade/Mark and Description
#Input grade: 87.6
#Grade/Mark: 1.75
#Description: Very Good

import math

#Introduction
def greetings():
    print ("Welcome to PUP Grading System Evaluator!")

#Rouding function
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier    

greetings()

#Grade input validation
def Grade_percentage():
    while True:
        try:
            Percentage = float(input("Enter your grade percentage here: "))
        except ValueError:
            print ("Sorry, your input is invalid")
            continue
        if Percentage < 0 or Percentage <=64 or Percentage >= 101:
            print ("ERROR, the input is below or above the grade limit")
            continue
        else:
            return Percentage
Valid_Grade = Grade_percentage()

#Grading system:
def Grades():
    Whole_Percentage = round_half_up(Valid_Grade)
    # Step 1 - 1.0 | Excellent
    if Whole_Percentage >= 97 and Whole_Percentage <=100:
        print ("Grade/Mark: 1.0")
        print ("Description: Excellent")
    # step 2 - 1.25 | Excellent
    elif Whole_Percentage >= 94 and Whole_Percentage <=96:
        print ("Grade/Mark: 1.25")
        print ("Description: Excellent")
    else:
        print ("Others")
        
Grades()