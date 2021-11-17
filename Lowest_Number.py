#Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number

#Step 1 - Ask for 3 Numbers
def Numbers():
    while True:
        try:
            global First, Second, Third 
            First = float(input("Enter your first number: "))
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
    if First < Second and Third:
        print (f"{First} is the lowest number.")
    else:
        print ("First number is not the lowest.")
lowest()
