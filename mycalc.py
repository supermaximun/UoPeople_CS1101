##Prompt for first number 
##Read first number and store in variable
num1 = int(input("Please enter a number:  "))

##Display operations (1-add, 2-subtract, 3-multiply, 4-divide)
print("Legal operations include:\n1-add\n2-subtract\n3-multiply\n4-divide")

##Prompt for operation 
##Read operation and store in variable 
oper_choice = int(input("Please select an operation (1, 2, 3 or 4):  "))

##Prompt for second number 
##Read second number and store in variable
num2 = int(input("Please enter a second number:  "))

## define result variable before use 
result = 0

##If operation is equal to 1 (add) 
##   Then 
##       Add first number to second number and store result in variable
if oper_choice == 1:
    result = num1 + num2
##Otherwise if operation is equal to 2 (subtract) 
##   Then 
##       Subtract second number from first number and store result in a variable
elif oper_choice == 2:
    result = num1 - num2
##Otherwise if operation is equal to 3 (multiply) 
##   Then 
##      Multiply first number with second number and store result in a variable
elif oper_choice == 3:
    result = num1 * num2
##Other wise if operation is equal to 4 (divide) 
##   Then 
##      Divide first number by the second number and store result in a variable 
elif oper_choice == 4:
    result = int(num1 / num2)

##Otherwise exit program
else:
    print("You didn't enter a valid operator")
##Display the result stored in the variable

print(result)

##Exit the program
