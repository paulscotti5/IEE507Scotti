import serial
from time import sleep

ser=serial.Serial('/dev/ttyUSB0',9600)
ser.reset_input_buffer()

while True:
#	if ser.in_waiting > 0:
	temp=ser.readline().decode('utf-8').rstrip()
	print(temp)
