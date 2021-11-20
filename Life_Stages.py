#Life stages
#Create a program that ask for an age of a person
#Display the life stage of the person.
#Rules:
#0 - 12 : Kid
#13 - 17 : Teen
#18 : Debut
#19 above : Adult

#Step 1 - input

def Age():
    while True:
        try:
            Age = int(input("Please enter your age: "))
        except ValueError:
            print ("Error, please input your age only.")
        if Age < 0:
            print ("Age can't be negative.")
        elif Age >= 0 and Age <= 12:
                print ("You're a kid.")
        elif Age >= 13 and Age <= 17:
                print ("You're a teen.")
        elif Age == 18:
                print ("You're debut.")
        elif Age >= 19:
                print ("You're an adult.")

Age()