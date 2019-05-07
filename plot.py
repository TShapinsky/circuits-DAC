#!/usr/bin/env python3
# coding=utf-8
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

xs, ys = [], []
with open(sys.argv[1]) as f:
    c = csv.reader(f, delimiter="\t")

    headers = next(c)  # Throw away the header
    series = {}
    for header in headers:
        series[header] = np.array([])
    for row in c:
        for i in range(len(row)):

            series[headers[i]] = np.append(series[headers[i]], float(row[i]))

series_to_plot = headers[1:] if sys.argv[2] == "*" else sys.argv[2:]
for data in series_to_plot:
    plt.plot(series["time"], series[data], ".", label=data)

plt.title("Simulated DAC characteristics")
plt.xlabel("Input Number")
plt.ylabel("Output voltage (V)")
plt.grid(True)
plt.legend()
plt.show()
