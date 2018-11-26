# C. Drew    ///   Final Exam, November 2018
# EE-629 Internet of Things   ///   Professor Kevin Lu
# Stevens Institute of Technology, Hoboken NJ
# TLDR: Take a CSV of Time-CPU%-Temp data and analyze it

import matplotlib.pyplot as plt
import numpy as np
import pylab as P
import pdb #what is this again, is it needed?
from pandas import *
from datetime import datetime

# Import the Data from the CSV
data = read_csv('data.csv')
cpu  = data['CPU Usage %']
temp = data['Temperature C']
time = np.array([datetime.datetime(data['Time'])])

# NOTE: TODO: Include title and labels and legend

# Time Series of Time-vs-CPU
plt.figure()
plt.plot(time,cpu)
plt.title('CPU Use -vs- Time')
plt.xlabel('Time [Absolute]')
plt.ylabel('CPU Use [%]')
plt.show()

# Time Series of Time-vs-Temperature

# Histogram of CPU

# Histogram of Temperature

# Box Plot of CPU
plt.figure()
plt.boxplot(cpu, 1, 'rs', 0)
plt.xlabel('CPU Usage [%]')
plt.title('Box Plot of CPU Usage')
plt.grid()
plt.show()

# Box Plot of Temperature

# Scatter Plot with Linear Regression

# Cross-validation prediction with temperature as target

#l = [slope * i + intercept for i in x]

