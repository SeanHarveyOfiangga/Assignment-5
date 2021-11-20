#Life stages
#Create a program that ask for an age of a person
#Display the life stage of the person.
#Rules:
#0 - 12 : Kid
#13 - 17 : Teen
#18 : Debut
#19 above : Adult

def greeting():
    print ("\nWelcome to Life stages app!\n")

greeting()

#Step 1 - input
def Age():
    #Step 2 input validation
    while True:
        try:
            Age = int(input("Please enter your age: "))
        except ValueError:
            print ("Error, please input your age only.")
        #Step 3 negative age is invalid
        if Age < 0:
            print ("Age can't be negative.")
        # Step 4 Kid age bracket
        elif Age >= 0 and Age <= 12:
                print ("You're a kid.")
                exit()
        # Step 5 Teen age bracket
        elif Age >= 13 and Age <= 17:
                print ("You're a teen.")
                exit()
        # Step 6 Debut age bracket
        elif Age == 18:
                print ("You're debut.")
                exit()
        # Step 7 Adult age bracket
        elif Age >= 19:
                print ("You're an adult.")
                exit()
            
        
Age()

