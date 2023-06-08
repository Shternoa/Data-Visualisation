import matplotlib.pyplot as plt

x_points = [1, 2, 3, 4, 5]
y_points = [2, 4, 9, 16, 26]
plt.scatter(x_points, y_points, s=50)

plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
