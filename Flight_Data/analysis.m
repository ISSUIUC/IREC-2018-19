%%

dataFile = load('dataFile.mat');
dataArray = dataFile.dataArray;

dataTicks = dataArray(1,:);
accelX = dataArray(2,:);
accelY = dataArray(3,:);
accelZ = dataArray(4,:);
temp = dataArray(5,:);
gyroX = dataArray(6,:);
gyroY = dataArray(7,:);
gyroZ = dataArray(8,:);

%% Time scaling

flight_ticks = 372390 - 370510;
flight_time = 158;  % seconds - from Telemtrum data

sec_per_tick = flight_time / flight_ticks;
ms_per_tick = sec_per_tick * 1000;
us_per_tick = ms_per_tick * 1000;

%%

plotStart = 370500;
plotEnd = 372500;

tStamp = (dataTicks(plotStart : plotEnd) - dataTicks(plotStart)) * ms_per_tick;

hold on
subplot(3,1,1)
plot(tStamp, accelX(plotStart: plotEnd), 'r')
legend("Accel X")
subplot(3,1,2)
plot(tStamp, accelY(plotStart: plotEnd), 'g')
legend("Accel Y")
subplot(3,1,3)
plot(tStamp, accelZ(plotStart: plotEnd), 'b')
legend("Accel Z")
hold off

