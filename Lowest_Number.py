#Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number

#Step 1 - Ask for 3 Numbers
def Numbers():
    while True:
        try:
            First = float(input("Enter your first number: "))
            Second = float(input("Enter your second number: "))
            Third = float(input("Enter your third number: "))
        except ValueError:
            print ("Please enter numbers only.")
            continue
        else:
            break
    
Numbers()