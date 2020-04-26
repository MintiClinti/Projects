a = float(input("Enter the a-coefficient. "))
b = float(input("Enter the b-coefficient. "))
c = float(input("Enter the c-coefficient. "))

first_x = (-b + ((b ** 2) - (4 * a * c)) ** (1 / 2)) / 2 * a
second_x = (-b - ((b ** 2) - (4 * a * c)) ** (1 / 2)) / 2 * a
discriminant = ((b ** 2) - (4 * a * c)) ** (1 / 2)

if isinstance(discriminant, complex):
    print("This function has no solution.")
else:
    print(first_x and second_x)

    


