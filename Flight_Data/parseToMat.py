# Simple parser that saves data as matlab matrix file

import matplotlib.pyplot as plt
import numpy as np
import scipy.io

filename = 'DATALOG.txt'

filehandle = open(filename, 'r')

ax, ay, az, temp, gx, gy, gz, starts, counters = [], [], [], [], [], [], [], [], []

counter = 0

for line in filehandle.readlines():
    data = line.split('\t')

    if data[0] != 'MMAAccelX ' and data[0] != 'm/s^2 ':
        ax.append(float(data[0]))
        ay.append(float(data[1]))
        az.append(float(data[2]))
        temp.append(float(data[3]))
        gx.append(float(data[4]))
        gy.append(float(data[5]))
        gz.append(float(data[6]))
        counters.append(counter)
        counter += 1

dataArray = np.array([counters, ax, ay, az, temp, gx, gy, gz])

scipy.io.savemat("dataFile.mat", mdict={'dataArray' : dataArray})
