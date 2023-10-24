import yfinance as yf
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from scipy.stats import skew, kurtosis
from sklearn.metrics import roc_curve, auc
from sklearn.datasets import load_iris
import csv
import shutil


# Specify the stock symbol and the desired date range
st = input("Que -accion? ")
desde= input("Desde que Fecha?(A-M-D) ")
hasta= input("Hasta que Fecha?(A-M-D) ")

stock_symbol = st
start_date = desde
end_date = hasta


# Retrieve the historical price data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

df1 = stock_data
df1.to_csv(f'{st}_datos.csv')

current_loc = f'{st}_datos.csv'
new_loc = '/media/alozan/cosas/Git/Support_Levels/Data/' + current_loc
shutil.copy(current_loc, new_loc)

def calculate_support_resistance(data):
    pivot_point = (data['High'] + data['Low'] + data['Close']) / 3
    support_l1 = (pivot_point * 2) - data['High']
    support_l2 = pivot_point - (data['High'] - data['Low'])
    resistance_l1 = (pivot_point * 2) - data['Low']
    resistance_l2 = pivot_point + (data['High'] - data['Low'])
    
    return pivot_point, support_l1, support_l2, resistance_l1, resistance_l2

pivot_point, support_l1, support_l2, resistance_l1, resistance_l2 = calculate_support_resistance(stock_data)

# Create a DataFrame to store the calculated levels
levels_data = pd.DataFrame({'Pivot Point': pivot_point,
                            'Support Level 1': support_l1,
                            'Support Level 2': support_l2,
                            'Resistance Level 1': resistance_l1,
                            'Resistance Level 2': resistance_l2})

df2= levels_data
df2.to_csv(f'{st}_levels.csv')

current_loc = f'{st}_levels.csv'
new_loc = '/media/alozan/cosas/Git/Support_Levels/Data/' + current_loc
shutil.copy(current_loc, new_loc)

plt.plot(levels_data);