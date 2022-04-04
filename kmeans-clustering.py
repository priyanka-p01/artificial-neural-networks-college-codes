# IPMV-E9: TO IMPLEMENT PATTERN CLUSTERING USING K-MEANS ALGORITHM
# AUTHOR - PRIYANKA S. PEDDINTI

# downloading libraries
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import pandas as pd
import numpy as np
# !pip install yellowbricks

dataset, classes = make_blobs(n_samples = 250, n_features = 2, centers = 4, cluster_std = 0.5, random_state = 0) 
df = pd.DataFrame(dataset, columns = ['var1', 'var2'])
df.head(6)
from pandas.core.common import random_state
model = KMeans()
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 0).fit(df)
kmeans.labels_

kmeans.inertia_
kmeans.cluster_centers_
from collections import Counter
Counter(kmeans.labels_)
import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(data = df, x = 'var1', y = 'var2', hue = kmeans.labels_)
plt.show()
sns.scatterplot(data = df, x = 'var1', y = 'var2', hue = kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker = 'X', c ='r', s = 80, label = 'centroids')
plt.legend()
plt.show()
