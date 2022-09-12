import numpy as np
import matplotlib.pyplot as plt

y1 = np.array([2,5,1,4,3,7,2])
x1 = y1 - 1
x2 = x1 + 1
y2 = (y1 + 3) / 2

params = {'marker':'o', 'ms':'10', 'mec':'#02dd01', 'mfc':'#9cea7f', 'ls':'',
          'lw':'7.5', 'c':'hotpink', }

font1 = {'family':'serif','color':'green','size':20}
font2 = {'family':'serif','color':'brown','size':15}

plt.plot(x1, y1, x2, y2, ls=params['ls'], marker=params['marker'])

plt.grid(c='brown', ls=':', lw="0.5")

plt.title("Practice Data", loc='left', fontdict=font1)
plt.xlabel("X Axis", fontdict=font2)
plt.ylabel("Y Axis", fontdict=font2)

plt.show()

x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y, c='red', s=100)

x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y, c='green', s=10)

plt.show()

x = ["Product A", "Product B", "Product C", "Product D"]
y = np.array([9, 8.5, 6, 9.5])

plt.bar(x, y, color="cyan")
plt.bar(x, y-1, width=0.1, color="red")

plt.show()

# create an array of 300 values, concentrating at 70, with SD of 4
x = np.random.normal(70, 4, 300)

# histogram has frequency on y-axis
plt.hist(x, color="cyan")

plt.show()

y = np.array([3, 1, 2, 5])
my_labels = ["X", "Y", "Z", "A"]
my_colors = ["g", "r", "b", "m"]

#explode tells how much to seperate a piece of the pie
my_explode = [0, 0, 0, 0.3]

#startangle tells where on the circle to start the first piece
plt.pie(y, labels=my_labels, colors=my_colors, explode=my_explode,
        startangle=90)

plt.legend(title="Products:")
plt.show()
