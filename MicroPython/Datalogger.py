import machine
import utime

sensor_temp = machine.ADC(4) #temp sensor in RP2040
conversion_factor = 3.3/(65535)

file = open("temps.txt", "w") #opens the file to write to

while True:
	reading = sensor_temp.read_u16() * conversion_factor
	temperatureC = 27 - (reading - .706)/.001721 #converts to degrees C
	temperatureF = (temperatureC * 9/5) + 32 #converts to degrees F
	
	file.write(str(temperatureF) + " F" + "\n") #write to the file
	file.flush() #temp data is committed to the file without closing it ("flushes" buffer data)

	utime.sleep(3) #10 sec buffer between readings


