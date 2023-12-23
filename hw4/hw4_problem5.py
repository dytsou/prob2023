#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sample code of HW4 Problem 5

"""

import numpy as np
import scipy
from scipy import stats
from scipy.stats import ecdf
import matplotlib.pyplot as plt

N = 10 ** 3
mu = 0
repeat = 100

Delta_A_list = []

#-------- Your code (~10 lines) ----------
for i in range(repeat):
    X = np.random.uniform(-1, 1, N)
    Y = np.random.uniform(-1, 1, N)
    in_range = (((X-0.25) ** 2 + 2 * ((Y+0.5) ** 2) <= 0.25) & (X+Y <= 0)).sum()
    Delta_A = 4 * (in_range / N)
    Delta_A_list.append(Delta_A)
estimate = np.mean(Delta_A_list)
    
#---------- End of your code -----------
# Optional: Print the Monte-Carlo estimates and visualize the empirical CDF
print(estimate)
res = stats.ecdf(np.array(Delta_A_list))
ax = plt.subplot()
res.cdf.plot(ax)
ax.set_xlabel('Estimated Delta_A')
ax.set_ylabel('Empirical CDF')
plt.show()