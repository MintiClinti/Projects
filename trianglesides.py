# sides of a triangle
side1, side2 = map(int, input('Enter two lengths of a triangle. I will give you a range for the 3rd side. ').split())
side31 = (side1 + side2) - 1
if side1 <= 0 or side2 <= 0:
    print("Those are not valid sides. ")
else:
    if side1 > side2:
        side32 = (side1 - side2) + 1
        print(f'Range of the 3rd side: {side32} < x < {side31}')
    else:
        side32 = (side2 - side1) + 1
        print(f'Range of the 3rd side: {side32} < x < {side31}')





