import matplotlib.pyplot as plt

x_points = list(range(1, 1001))
y_points = [x ** 2 for x in x_points]
plt.scatter(x_points, y_points, c='purple', edgecolors='none', s=50)

plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.show()
