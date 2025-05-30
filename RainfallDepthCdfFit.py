
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon

plt.rcParams['font.sans-serif'] = ['SimSun']  
plt.rcParams['font.serif'] = ['Times New Roman']  

plt.rcParams['font.size'] = 18
data_list = []
filepath=''
with open(filepath, 'r') as file:
    for line in file:
        
        data_list.append(float(line.strip()))


x = np.sort(data_list)
y = np.arange(1, len(data_list) + 1) / len(data_list)


plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='', label = 'rainfall depth sample')


loc, scale = expon.fit(data_list)
cdf_fit = expon.cdf(x, loc, scale)
plt.plot(x, cdf_fit, color='r', label='CDF')


plt.xlabel('Rainfall depth(mm)')
plt.ylabel('CDF')

plt.legend(loc='lower right')
plt.subplots_adjust(left=0.11, bottom=0.13, right=0.97, top=0.95)
plt.text(x=8, y=0.92, s='A pattern', fontsize=18, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

plt.text(0.7, 0.3, f'fitting parameters:\nlocation parameter={loc:.2f}\nscale parameter={scale:.2f}',
         transform=plt.gca().transAxes, fontsize=18, verticalalignment='center')

plt.grid(True)
plt.savefig('cdf_plot.jpg', dpi=500)
plt.show()