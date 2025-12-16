import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame

x = df['sepal length (cm)']
y = df['petal length (cm)']
plt.scatter(x, y)
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Simple Correlation Plot')

plt.savefig('correlation.png')
plt.show()

