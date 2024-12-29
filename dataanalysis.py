print("hello world")

import pandas as pd # importing libraries to use when coding graphs
import matplotlib.pyplot as plt

data = pd.read_csv('animals_info.csv') #importing data set
print("Here are the first few animals")
print(data.head()) #testing to see if dataset has been imported

print("Comments added")
