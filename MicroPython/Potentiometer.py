import machine
import utime

#configure first channel
potentiometer = machine.ADC(26) #GP 26 should be used with analog digital converter (ADC)

conversion_factor = 3.3 / (65535) #voltage/ range of values = resolution in bits

#read the input
while True:
	voltage = potentiometer.read_u16() * conversion_factor
	#Note: read_u16 means that instead of a bool it should be looking for an unsigned 16-bit integer- a wide range of values

	print(voltage) 
	utime.sleep(.1)