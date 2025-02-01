# Eshjot Singh (Question-2)
def validation(user_input): #creating a function validation and adding a parameter
    if user_input.isdigit():
        if 1 <= int(user_input)  <=100:  #using if condition for checking the user input is between 1 and 100
            return True
    return False
   
while True:
    user_input=(input("Enter a number between 1 and 100: \n"))   #value is entered by the user in variable user_input
    if validation (user_input) :  #if condition to check number is valid between 1 and 100
        print("The number you entered is valid")  
        break
    else:
        print("The number you entered is not valid") 