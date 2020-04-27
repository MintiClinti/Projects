num_1 = float(input("Enter a number. "))
num_2 = float(input("Enter a second number. "))
operation = input("Enter an operation-add, subtract, multiply, divide, exponent, root. The second number is the exponent or index. ")
            

if operation == "add":
    print(num_1 + num_2)
elif operation == "subtract":
    print(num_1 - num_2)
elif operation == "multiply":
    print(num_1 * num_2)
elif operation == "divide":
    print(num_1 / num_2)
elif operation == "exponent":
    print(num_1 ** num_2)
elif operation == "root":
    print(num_1 ** (1 / num_2))
else:
    print("That is not a valid operation.")
            
