#!/usr/bin/env python3
# coding=utf-8
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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

y_start = 2.76632
y_end = 2.26696
x_start = 0.5
x_end = 63.5

m = (y_end - y_start) / (x_end - x_start)
b = y_start - m * x_start

fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(111)
ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("0b{x:06b}"))
ax.xaxis.set_ticks(np.arange(0, 64, 8))

plt.plot(series["time"], series["V(vout)"], "-", label="Output voltage")
plt.plot(series["time"], m * series["time"] + b, "-", label="Ideal slope")

plt.title("Simulated DAC characteristics")
plt.xlabel("Time (s)")
plt.ylabel("Output voltage (V)")
plt.grid(True)
plt.legend()

# plt.show()
plt.savefig("vout.pdf")
plt.cla()
