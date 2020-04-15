#Program name: Wk2P1BenVance.py
#Student Name: BenVance
#Course: ENTD220
#Instructor: Robert Haluska
#Date: 4/13/2020

#This function performs additiion
def add(num1, num2):
  return num1 + num2

#This function performs subtraction
def subtraction(num1, num2):
  return num1 - num2

#This function performs multiplication
def multiply(num1, num2):
  return num1 * num2

#This function performs division
def divide(num1, num2):
  return num1 / num2

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print(num1,"+",num2,"=", add(num1, num2))
print(num1,"-",num2,"=", subtraction(num1, num2))
print(num1,"*",num2,"=", multiply(num1, num2))
print(num1,"/",num2,"=", divide(num1, num2))
