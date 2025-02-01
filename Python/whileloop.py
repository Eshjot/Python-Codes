while  True: #Initiating with while loop

    a = int(input("Enter your 1st number"))  #Entering the values from user
    b = int(input("Enter your 2nd number"))
    sum = a+b #sum of a and b stored in variable sum
    print("The sum of both value is", sum) #printing the sum

    decision=input("Do you wish to perform operation again? (yes or no): ") #making choice to run program again and again
    if decision!='yes': #using if statement to make decision
        break
    