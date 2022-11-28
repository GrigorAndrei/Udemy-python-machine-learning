import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_modeal import LinearRegression
from sklearn.metrics import mean_squared_error
import math

house_data = pd.read_csv("house-prices.csv")
size = house_data['SqFt']
price = house_data['median_house_value']
