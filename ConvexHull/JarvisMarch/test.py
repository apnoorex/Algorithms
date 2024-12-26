from matplotlib import pyplot as plt
from random import randint
from jarvis_march import jarvis_march


def create_points(n_points, min=0, max=20):
	return [[randint(min, max), randint(min, max)] for _ in range(n_points)]

x = create_points(17)
hull = jarvis_march(x)
print('Hull:', hull)

# Plot the result
xs, ys = zip(*x)
fig, ax = plt.subplots(figsize=(6, 6))
ax.spines['top'].set_color('#ffffff') 
ax.spines['right'].set_color('#ffffff')
plt.scatter(xs, ys)

for i in range(1, len(hull) + 1):
    if i == len(hull): i = 0
    c0 = hull[i - 1]
    c1 = hull[i]

    plt.plot((c0[0], c1[0]), (c0[1], c1[1]), '#E0AA8E')

plt.show()
