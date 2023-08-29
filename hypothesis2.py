# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:09:22 2023

@author: user
"""

import numpy as np
from scipy.stats import ttest_ind
A1=np.array([11,12,13,14,15])
A2=np.array([21,25,56,14,28])
A3=np.array([33,36,37,38,39])
t_stats, p_value = ttest_ind(A1,A2)
if p_value < 0.05:
    print("Its NULL Hypothesis")
else:
    print("Fail to test NULL Hypothesis")
