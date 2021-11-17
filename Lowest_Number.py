#Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number


#Introduction
def greeting():
    print ("\nWelcome to find the lowest number app!")

greeting()

#Step 1 - Ask for 3 Numbers
def Numbers():
    while True:
        try:
            global First, Second, Third 
            First = float(input("\nEnter your first number: "))
            Second = float(input("Enter your second number: "))
            Third = float(input("Enter your third number: "))
        except ValueError:
            print ("Please enter numbers only.")
            continue
        else:
            break
    
Numbers()

#Step 2 - If else statement
def lowest():
    if First < Second and First < Third:
        print (f"\n'{First}' first number is the lowest.")
    elif Second < First and Second < Third:
        print (f"\n'{Second}' second number is the lowest.")
    elif Third < First and Third < Second:
        print (f"\n'{Third}' third number is the lowest.")
        
lowest()

def Outro():
    print ("\nThank you for using the lowest number app!")

Outro()