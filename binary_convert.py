num = int(input("Enter a number. "))
binum = [num % 2]

while num > 1:
    num = num // 2
    remainder = (num % 2)
    binum.append(remainder)
    
print(binum[::-1])

