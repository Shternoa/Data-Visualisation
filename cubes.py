import matplotlib.pyplot as plt

# input_cubes = [1, 2, 3, 4, 5]
# cubes = [1, 8, 27, 64, 75]
x_cubes = list(range(1, 5001))
y_cubes = [x ** 3 for x in x_cubes]
color = list(range(len(x_cubes)))
plt.scatter(x_cubes, y_cubes, c=color, cmap=plt.cm.Reds, edgecolors='none', s=30)

# Заголовок программы и метка осей
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
