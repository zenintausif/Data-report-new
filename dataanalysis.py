print("hello world")

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('animals_info.csv')
print("Here are the first few animals")
print(data.head())
