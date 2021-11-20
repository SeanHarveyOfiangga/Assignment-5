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
    Age = int(input("Please enter your age: "))
    if Age >= 0 and Age <= 12:
        print ("You're a kid.")
    else:
        print ("Others.")

Age()