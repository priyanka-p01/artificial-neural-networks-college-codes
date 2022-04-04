# IPMV-E7: TO IMPLEMENT CLASSIFICATION OF RANDOM NUMBERS USING SUPPORT VECTOR MACHINE ALGORITHM
# AUTHOR - PRIYANKA S. PEDDINTI


# DOWNLOADING LIBRARIES - as in Jupyter notebook in Google collab
from sklearn.datasets import make_blobs
import numpy as np
import pandas as pd

from sklearn.datasets import make_blobs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#plotting scatters
X, Y = make_blobs(n_samples = 550, centers = 3, random_state = 0, cluster_std = 0.60)
plt.scatter(X[:,0], X[:, 1], c = Y, s=50, cmap = 'spring')
plt.show()

# creating line spce between -1 to 3.5

xfit = np.linspace(-1, 3.5)

#plotting scatter
X, Y = make_blobs(n_samples = 550, centers = 3, random_state = 0, cluster_std = 0.75)
plt.scatter(X[:, 0], X[:, 1], c = Y, s = 50, cmap = 'spring')

# to plot a line between the data sets

for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
  yfit = m *xfit + b
  plt.plot(xfit, yfit, '-k')
  plt.fill_between(xfit, yfit - d, yfit + d, edgecolor = 'none',
  color = '#AAAAAA', alpha = 0.4)

plt.xlim(-1, 3.5)
plt.show()
