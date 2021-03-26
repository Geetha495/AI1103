# -*- coding: utf-8 -*-
"""Assignment4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FEfT08AVuL5VUd-AIIxXAw2zBqz4DYbf
"""

from scipy.stats import bernoulli


Pr_A = 1/2
Pr_B = 33/100
Pr_C = 1/5

#Theoritcal
Pr_AB = 16/100
Pr_BC = 6/100
Pr_AC = 1/10
Pr_ABC=3/100
theor_prob = 1 - Pr_A - Pr_B - Pr_C + Pr_AB + Pr_BC + Pr_AC - Pr_ABC

#Simulation
size=int(1e7)

data_A = bernoulli.rvs(p = Pr_A , size = size)
data_B = bernoulli.rvs(p = Pr_B , size = size)
data_C = bernoulli.rvs(p = Pr_C , size = size)

count_required =0

for i in range(size):
  if not ( (data_A[i] ==1 ) or (data_B[i] ==1) or (data_C[i] ==1) ) :
    count_required+=1
  
calc_prob = count_required/size

print(f"For Pr((A+B+C)') , theoritical and calculated values are {theor_prob} , {calc_prob} respectively")