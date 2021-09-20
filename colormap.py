import matplotlib.pyplot as plt

""" Simple function to plot the first five,
and the first 5 thousand cubic numbers, and apply a color map"""

n =int(input("enter either 6 or 50001 "))

x_values = list(range(n))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.show()

