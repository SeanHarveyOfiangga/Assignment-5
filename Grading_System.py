#Program 1: PUP Grading System
#Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
#Create a program that will ask for grade percentage. 
#Display the equivalent Grade/Mark and Description
#Input grade: 87.6
#Grade/Mark: 1.75
#Description: Very Good

import math

def greetings():
    print ("Welcome to PUP Grading System Evaluator!")

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier    

#Grade percentage
def Grade_percentage():
    Percentage = float(input("Enter your grade percentage here: "))
    Whole_Percentage = round_half_up(Percentage)
    print (Whole_Percentage)
        
greetings()
Grade_percentage()