# Taking 2 inputs from user

number1 = int(input("Enter number: "))
number2 = int(input("Enter another number: "))

quotient = int(number1 / number2)
remainder = number1 - (number2 * quotient)
#quotient = number1 // number2
#remainder = number1 % number2
print(quotient)
print(remainder)
