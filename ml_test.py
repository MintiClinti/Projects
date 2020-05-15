from scipy import stats
import matplotlib.pyplot as mpl

x = [1, 22, 40, 17, 43, 35, 39, 16, 38, 8]
y = [82, 110, 137, 115, 135, 133, 140, 117, 136, 100]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def predictor(x):
    return slope * x + intercept

length = int(input("How long is the walk? (in minutes) "))
heart_rate = int(predictor(length))
best_fit = list(map(predictor, x))
print(f"The estimated heart rate is {heart_rate} beats per minute.")

mpl.scatter(x, y)
mpl.plot(x, best_fit)
mpl.show()
