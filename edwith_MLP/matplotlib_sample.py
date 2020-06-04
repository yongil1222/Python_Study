import matplotlib.pyplot as plt

x = range(100)
y = [value**2 for value in x]

plt.plot(x,y)
plt.show()