import serial
from time import sleep

ser=serial.Serial('/dev/ttyUSB0',9600)
ser.reset_input_buffer()

class temperatura:
	def __init__(self,celsius):
		self.celsius=celsius

	def getCelsius(self):
		print("La temperatura es: ", self.celsius)



while True:
	temp=temperatura(ser.readline().decode('utf-8').rstrip())
	temp.getCelsius()
