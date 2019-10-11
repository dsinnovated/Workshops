"""
Created on Fri Oct 11 01:40:04 2019 
Not even going to hide the fact that this was done at 1am
@author: Vince
"""
# Example program to learn Kmeans Clustering
# Most of this code can be found https://medium.com/@belen.sanchez27/predicting-iris-flower-species-with-k-means-clustering-in-python-f6e46806aaee


# Import packages - The "from" keyword tells your program to look for a function or collection in the package 
# This reduces the amount of code you have to load into your program => faster runtime and memory useage since we do not need everythign in the package
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# Popular dataset from: https://archive.ics.uci.edu/ml/datasets/Iris is part of a package in SKLearn
# You can alternatively download it (but its already in SKLearn so why redownload)
iris = datasets.load_iris()


#Calling this print will actually print more than just the dataframe because its bunched up with other information (metadata)
#print(iris)

# If you open up the iris variable in the variable explorer you will see what attributes it has:
# It contains a Key [DESCR, data, feature_names, filename, target, target_names]
# Type (basically tells you what data type the key is)
# Size (size of the key:: the important ones to look for is data and target)
# target (classifications : 0,1,2)
# target_names (setosa = 0, versicolor =1, virginica =2)

X = iris.data[:, :2]        # iris is a matrix. we are only interested in the data to store as our X 
                            # data[] is also a matrix of 150x4. This command means we want all rows, and all columns from 0-1 (in python ranges is always -1 from ending number)
y = iris.target             # similarly we are interested in storing target as our output or "target" 
                            # Check our variable explorer or simply print X or y and see what our data looks like

# We're going to call a function in matplot to create a scatter plot to visualize the first 2 columns of X
# Documentation for scatter : https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html
plt.scatter(X[:,0], X[:,1], c=y, cmap='gist_rainbow')
plt.xlabel('Sepa1 Length', fontsize=18)
plt.ylabel('Sepal Width', fontsize=18)



# Now let's start clustering
# Again documentation if you need it: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
km = KMeans(n_clusters = 3, n_jobs = 4, random_state=21)        # Here we just define the K-number of clusters, 
km.fit(X)                                                       # Fit the model

centroids = km.cluster_centers_                                 # The centers are stored in this field we want to just assign it to a variable for ease of access
print(centroids)                          

new_labels = km.labels_                                         # Based on the centroids we assign a label or a class 

fig, axes = plt.subplots(1, 2, figsize=(16,8))                  # make 2 parallel plots(0- actual 1- predicted)
axes[0].scatter(X[:, 0], X[:, 1], c=y, cmap='gist_rainbow', edgecolor='k', s=150)   # Actual plot of data
axes[1].scatter(X[:, 0], X[:, 1], c=new_labels, cmap='jet',edgecolor='k', s=150)    # Prediction
axes[0].set_xlabel('Sepal length', fontsize=18)
axes[0].set_ylabel('Sepal width', fontsize=18)
axes[0].tick_params(direction='in', length=10, width=5, colors='k', labelsize=20)
axes[1].tick_params(direction='in', length=10, width=5, colors='k', labelsize=20)
axes[0].set_title('Actual', fontsize=18)
axes[1].set_title('Predicted', fontsize=18)











