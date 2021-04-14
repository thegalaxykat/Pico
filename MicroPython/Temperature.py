import machine
import utime

sensor_temp = machine.ADC(4) #temp sensor in RP2040
conversion_factor = 3.3/(65535)

while True:
	reading = sensor_temp.read_u16() * conversion_factor
	temperatureC = 27 - (reading - .706)/.001721 #converts to degrees C
	temperatureF = (temperatureC * 9/5) + 32 

	print(temperatureC)
	utime.sleep(2)