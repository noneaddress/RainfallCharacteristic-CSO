
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, pearson3

plt.rcParams['font.serif'] = ['Times New Roman']

plt.rcParams['font.size'] = 18
data_list = []
filepath=''
with open(filepath, 'r') as file:
    for line in file:
        # Convert the floating-point number of each row to an element in the list
        data_list.append(float(line.strip()))

shape, loc, scale = pearson3.fit(data_list)
x = np.linspace(pearson3.ppf(0.01, shape, loc, scale), pearson3.ppf(0.99, shape, loc, scale), 100)

plt.figure(figsize=(8, 6))
plt.hist(data_list, bins=20, density=True, alpha=0.6, color='g', label='Data') # plot histgram
plt.plot(x, pearson3.pdf(x, shape, loc, scale), 'r-', lw=2, label='Fitted Pearson III') # curve fitting plot
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Fitting Pearson III Distribution')
plt.legend()
plt.grid(True)
plt.show()

