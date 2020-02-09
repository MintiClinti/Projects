weight_pound = int(input("How much do you weigh? In pounds: "))
height_inch = int(input("How tall are you? In inches: "))

bmi = 703 * weight_pound / pow(height_inch, 2)
if bmi <= 18.5:
    print("Your BMI is " + str(bmi) + ", which means you are underweight")
elif bmi > 18.5 and bmi <= 24.9:
    print("Your BMI is " + str(bmi) + ", which means you are normal")
elif bmi > 25 and bmi < 29.9:
    print("Your BMI is " + str(bmi) + ", which means you are overweight")
else:
    print("Your BMI is " + str(bmi) + ", which means you are obese")
