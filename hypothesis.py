# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy.stats import ttest_ind
A1=np.array([11,12,13,14,15])
A2=np.array([21,25,56,14,28])
t_stats, p_value = ttest_ind(A1,A2)
if p_value < 0.05:
    print("Its NULL Hypothesis")
else:
    print("Fail to test NULL Hypothesis")
