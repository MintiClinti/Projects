num = int(input("Enter a number. "))
binum = [num % 2]

def binary_convert(num):
    if num < 0:
        return("We don't handle negatives. Sorry.")
    else:
        while num > 1:
            num = num // 2
            remainder = (num % 2)
            binum.append(remainder)
        return(binum[::-1])

print(binary_convert(num))
