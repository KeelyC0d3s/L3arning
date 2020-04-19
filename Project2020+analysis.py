#Iris Dataset Project 2020 Programming and Scripting GMIT



#Fisher’s Iris Dataset
#Introduced by British statistician and biologist Ronald Fisher in his 1936 paper entitled “The use of multiple measurements in taxonomic problems”. It is an example of linear discriminate analysis.
#The dataset gives the measurements in centimetres of the sepal length and width and petal length and width of 50 flowers from each species of iris: setosa, versicolor, and virginica.
#The dataset contains a set of 150 records of 5 attributes:
#Sepal length in cm
#Sepal width in cm
#Petal length in cm
#Petal width in cm
#Species of iris: setosa, versicolor, virginica




#Libraries used: pandas, Numpy, seaborn
import pandas as pd
import numpy as numpy
import seaborn as sns

#Downloaded iris dataset from https://tinyurl.com/y8fovkyq

iris_data = pd.read_csv('tableconvert_csv_xin5ac.csv')

iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

iris_data.head(10)
