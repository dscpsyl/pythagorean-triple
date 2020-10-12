import numpy as np
#Calculations
def calculation1(real, imaginary):
    one = real**2 - imaginary**2
    two = 2 * real * imaginary 
    three = real**2 + imaginary**2
    return str(one) + "," + str(two) + "," + str(three)
    
################################ https://www.youtube.com/watch?v=QJYmyhnaaek
#main terminal prompts
if __name__ == "__main__":
    print("Welcome to the simple pythagorean triple finder. To get started...")
    again = True
    while again:
        inputCorrect = True
        while inputCorrect:
            real = input("Choose a random number: ")
            imaginary = input("Choose another random number: ")
            try:
                real = int(real)
                imaginary = int(imaginary)
            except:
                print("Please only input intergers. Try again")
            inputCorrect = False
        result1 = calculation1(real, imaginary)
        print("Your generated pythagorean triple is:")
        print(result1, end="\n")
        oneMoreTime = input("Would you like to go again?\npress 'y' for yes or any other key for no: ")
        if oneMoreTime != "y":
            again = False
        
