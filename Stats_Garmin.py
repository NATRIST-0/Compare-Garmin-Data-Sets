#!/usr/bin/python3
# author: Tristan Gayrard

"""
Stats_Garmin
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

data = pd.read_excel(r"C:\Users\GAYRARD\Desktop\flight_test.xlsx")

df = pd.DataFrame(data)

df1 = [df['X1 (m)'], df['Y1 (m)'], df['Z1 (m)']]

df2 = [df['X2 (m)'], df['Y2 (m)'], df['Z2 (m)']]

df3 = df['X1 (m)'] - df['X2 (m)'], df['Y1 (m)'] - df['Y2 (m)'], df['Z1 (m)'] - df['Z2 (m)']

c = np.sqrt((df3[0])**2 + (df3[1])**2 + (df3[2])**2)

mean_error = np.mean(c)
std_dev_error = np.std(c)

fig, axs = plt.subplots()
fig.patch.set_linewidth(5)
fig.patch.set_edgecolor('slategrey')

plt.hist(c, weights=np.ones(len(data)) / len(data), bins=30, color='coral', edgecolor='black')

plt.title('Positional error derived from localization using speed and GPS data', fontsize=18)
plt.xlabel('||C||₂ (m)', fontsize=12)
plt.ylim([0, 0.27])
plt.gca().yaxis.set_major_formatter(PercentFormatter(1)) # to print ex : 25% instead of 0.25 on y axis
plt.axvline(mean_error, color='steelblue', linestyle='dashed', linewidth=1, label=f'Mean error: {mean_error:.1f} m')
plt.fill_between([mean_error - std_dev_error, mean_error + std_dev_error], 0, 1, color='crimson', alpha=0.3, label=f'±Std Dev: {std_dev_error:.1f} m')
plt.legend()
plt.show()
