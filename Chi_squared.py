# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 12:24:58 2016

@author: Chang
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import collections

# import data and clean data
df =pd.read_csv('/Users/Chang/Desktop/data_science/loansData.csv')

df = df.dropna()

freq =collections.Counter(df['Open.CREDIT.Lines'])
chi,p = stats.chisquare(freq.values())

plt.bar(freq.keys(),freq.values(),width=1)
plt.show()

print("The X^2 value is {}".format(str(chi)))
print("The P value is {}".format(str(p)))





'''
# generate boxplot and histogram
df.boxplot(column='Amount.Requested')
df.hist(column='Amount.Requested',bins=20)

# generate QQ plot to test normality of data
fig =plt.figure(figsize=(6,6))
pp = stats.probplot(df['Amount.Requested'],dist='norm',plot=plt)
plt.show()'''