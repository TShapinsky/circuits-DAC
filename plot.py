#!/usr/bin/env python3
# coding=utf-8
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

xs, ys = [], []
with open(sys.argv[1]) as f:
    c = csv.reader(f, delimiter="\t")
    
    headers = next(c) # Throw away the header
    series = {}
    for header in headers:
        series[header] = np.array([])
    for row in c:
        for i in range(len(row)):
            
            series[headers[i]] = np.append(series[headers[i]],float(row[i]))

for data in sys.argv[2:]:
    if data == '*':
        for header in headers[1:]:
            plt.plot(series['time'],series[header],'.', label=header)
        continue
    plt.plot(series['time'], series[data], '.', label=data)
plt.legend()
plt.show()

