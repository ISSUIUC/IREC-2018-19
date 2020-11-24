import matplotlib.pyplot as plt
import numpy as np
#from kalman_example import kalman_xy

#filename = '\\\\ad.uillinois.edu\\engr-ews\\ayberky2\\Documents\\GitHub\\irec_data\\DATALOG_2.txt'
filename = 'DATALOG_2.txt'

filehandle = open(filename, 'r')

ax, ay, az, temp, gx, gy, gz, starts, counters = [], [], [], [], [], [], [], [], []

counter = 0

def convertAccel(input):
    return float(input) * 9.81 / 1024

for line in filehandle.readlines():
    data = line.split('\t')

    if counter >= 39700 and counter <= 41800 and data[0] != 'MMAAccelX ' and data[0] != 'm/s^2 ':
        ax.append(float(convertAccel(data[0])))
        ay.append(float(convertAccel(data[1])))
        az.append(float(convertAccel(data[2])))
        temp.append(float(convertAccel(data[3])))
        gx.append(float(convertAccel(data[4])))
        gy.append(float(convertAccel(data[5])))
        gz.append(float(convertAccel(data[6])))
        counters.append(counter)

    elif counter >= 2 and (data[0] == 'MMAAccelX ' or data[0] == 'm/s^2 '):
        starts.append(counter)

    counter += 1

fig, axs = plt.subplots(4, 1)
axs[0].plot(counters, ax, 'r', linewidth = 0.3)
axs[0].set_ylabel('AccelX')
axs[0].grid(True)

axs[1].plot(counters, ay, 'g', linewidth = 0.3)
axs[1].set_ylabel('AccelY')
axs[1].grid(True)

axs[2].plot(counters, az, 'b', linewidth = 0.3)
axs[2].set_ylabel('AccelZ')
axs[2].grid(True)

axs[3].plot(counters, gx, 'r', linewidth = 0.3)
axs[3].set_ylabel('GyroX')
axs[3].grid(True)

# plt.xlim(39500, 42500)

plt.show()
