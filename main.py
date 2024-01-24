import math
print("This is a calculator! It can solve addition, subtraction, multiplication, division, and square root problems, and can also print the first 17 digits of pi.")
while True:
    oper = input("Enter your operator! ")

    if oper == "/":
        num1 = input("Enter the first number of your math question! ")
        num2 = input("Enter the second number of your math question! ")
        if str(num1).find("."):
            num1 = float(num1)
        else:
            num1 = int(num1)
        if str(num2).find("."):
            num2 = float(num2)
        else:
            num2 = int(num2)
        print(str(num1) + " / " + str(num2) + " = " + str((num1 / num2)))
    elif oper == "*" or oper == "x" or oper == "X":
        num1 = input("Enter the first number of your math question! ")
        num2 = input("Enter the second number of your math question! ")
        if str(num1).find("."):
            num1 = float(num1)
        else:
            num1 = int(num1)
        if str(num2).find("."):
            num2 = float(num2)
        else:
            num2 = int(num2)
        print(str(num1) + " * " + str(num2) + " = " + str((num1 * num2)))
    elif oper == "+":
        num1 = input("Enter the first number of your math question! ")
        num2 = input("Enter the second number of your math question! ")
        if str(num1).find("."):
            num1 = float(num1)
        else:
            num1 = int(num1)
        if str(num2).find("."):
            num2 = float(num2)
        else:
            num2 = int(num2)
        print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
    elif oper == "-":
        num1 = input("Enter the first number of your math question! ")
        num2 = input("Enter the second number of your math question! ")
        if str(num1).find("."):
            num1 = float(num1)
        else:
            num1 = int(num1)
        if str(num2).find("."):
            num2 = float(num2)
        else:
            num2 = int(num2)
        print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
    elif oper == "√" or oper == "sqrt":
        numSqrt = input("Input your number! ")
        if str(numSqrt).find("."):
            numSqrt = float(numSqrt)
        else:
            numSqrt = int(numSqrt)
        print("√" + str(numSqrt) + " = " + str(math.sqrt(numSqrt)))
    elif oper == "pi" or oper == "π":
        print("These are the first 17 digits of pi: " + str(math.pi))
    else:
        print("Whoops! Your operator is invalid or not yet implemented.")