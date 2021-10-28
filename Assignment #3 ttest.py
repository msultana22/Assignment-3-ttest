#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:34:26 2021

@author: mahbubasultana
"""

import pandas as pd 
from scipy.stats import shapiro
from matplotlib import pyplot
import scipy.stats as stats
from scipy.stats import ttest_ind

# dataframe
diabetes = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv")

diabetes_small = diabetes.sample(100)

## Generate lists of var names 
lits(diabetes_small)


## T test 

# 1) Is there a difference between sex (M:F) and the number of days in hospital?

list(diabetes)

Female = diabetes[diabetes['gender'] == 'Female']
Male = diabetes[diabetes['gender'] == 'Male']

ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])

## Ttest_indResult(statistic=9.542637042242887, pvalue=1.4217299655114968e-21)
# There is a significant difference between the P-value and the Statistic value and both very large so we do not have enough evidence to reject the null


## 2) Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?

Caucasian = diabetes[diabetes['race'] == 'Caucasian']
AfricanAmerican = diabetes[diabetes['race'] == 'AfricanAmerican']

ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital'])

##  Ttest_indResult(statistic=-5.0610017032095325, pvalue=4.178330085585203e-07)
# There is a significant difference between the P-value and the Statistic value and both very large so we do not have enough evidence to reject the null


## 3) Is there a difference between RACE (Asian and African American) and the number of lab procedures performed?

Asian = diabetes[diabetes['race'] == 'Asian']
AfricanAmerican = diabetes[diabetes['race'] == 'AfricanAmerican']

ttest_ind(Asian['num_lab_procedures'], AfricanAmerican['num_lab_procedures'])

## Ttest_indResult(statistic=-3.9788715315360292, pvalue=6.948907528800307e-05)
# # There is a significant difference between the P-value and the Statistic value and both very large so we do not have enough evidence to reject the null


