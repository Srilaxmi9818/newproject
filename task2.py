age = 26                            #create a variable ageand set it to your age
print ("I am",age,"years old")
name = "Sreelakshmi"                #create a variable named name and set it to your name
print ("My name is",name)

fruits = ['banana','apple','orange']      #create a list with 3 fruits name
coordinates = (3, 5)                    #create a tuple with x and y coordinates
person = {'name':'age'}                   #create a dictionary with name and age as key value pairs

#Write  a program asking the userto input their name and favourite colour and then prints them
user_name = input("Enter your name:")
favourite_colour = input("Enter your favourite colour:")
print ("Hello",user_name,"your favourite colour is",favourite_colour)

#Ask the user for a number and print the square of that number
number = int (input("Enter the number to be squared:"))
result = number*number
print ("The square of",number,"is",result)

#Write a program that asks for 2 numbers and prints their sum, difference, product and quotient
number1 = int(input("Enter first number:"))
number2 = int(input("Enter the second number:"))
sum = number1 + number2
difference = number1 - number2
product = number1 * number2
quotient = number1 / number2
print ("Sum is",sum)
print ("Difference is",difference)
print ("Product is",product)
print ("Quotient is",quotient)

#Compare 2 numbers and print which is larger or if they are equal
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
if (num1>num2):
    print ("Larger number is",num1)
elif (num1<num2):
    print ("Larger number is",num2)
else:
    print ("They are equal")
    

