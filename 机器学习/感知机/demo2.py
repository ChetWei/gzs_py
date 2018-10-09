from sklearn.datasets import load_iris
data = load_iris()
data.data[[10, 25, 50]]
data.target[[10, 25, 50]]
list(data.target_names)
list(data.feature_names)


print(data)

