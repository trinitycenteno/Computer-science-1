'''
build a calculator that provides the amount of miles per gallon

miles per gallon = miles driven/gallons used

'''

while True: 
    print("this program calculates mpg.")
    miles_driven = float(input("please enter the amount of miles driven:"))
    gallons_used = float(input("enter gallons used:"))
    mpg= miles_driven / gallons_used
    print("your miles per gallon is", mpg)
    user_input= input("would you like to perform a new calculation? Y/N")
    if user_input== "Y" or user_input=="y":
        continue
    else:
        break
    
