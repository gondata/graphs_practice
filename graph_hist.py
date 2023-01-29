import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.genfromtxt('dist.csv', delimiter=',')

sns.histplot(data)
plt.title('Distribution')
plt.show()