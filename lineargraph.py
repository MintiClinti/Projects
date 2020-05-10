import matplotlib.pyplot as mpl

x1 = float(input("Enter the first x value. "))
y1 = float(input("Enter the first y value. "))
x2 = float(input("Enter the second x value. "))
y2 = float(input("Enter the second y value. "))

point1 = [x1, y1]
point2 = [x2, y2]

x = [point1[0], point2[0]]
y = [point1[1], point2[1]]

slope = (x2 - x1) / (y2 - y1)
y_int = (y1 - (slope * x1))

mpl.xlim(-10, 10)
mpl.ylim(-10, 10)
mpl.plot(x, y, 'bo-')
mpl.show()

print(f"The equation of this line is {slope}x + {y_int}.")



