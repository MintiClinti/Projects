convert = input("0 for fahrenheit to celsius and 1 for celsius to fahrenheit. ")

if convert == "0":
    f_c = int(input("Enter a temperature in celsius. "))
    print(f_c * (9/5) + 32)
elif convert == "1":
    c_f = int(input("Enter a temperature in fahrenheit. "))
    print((c_f - 32) * (5 / 9))
else:
    print("That is not a valid statement.")
    
    
    
