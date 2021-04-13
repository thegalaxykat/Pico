import machine
import utime

#configure first channel
potentiometer = machine.ADC(26) #GP 26 should be used with analog digital converter (ADC)

led = machine.PWM(machine.Pin(15)) #activates PWM (pulse-width modulation) on GP 15 (channel 7)
led.freq(1000) #sets freqency of PWM on led to 1000 hz

conversion_factor = 3.3 / (65535) #voltage/ range of values = resolution in bits

#read the input
while True:
	voltage = potentiometer.read_u16() * conversion_factor
	#Note: read_u16 means that instead of a bool it should be looking for an unsigned 16-bit integer- a wide range of values

	led.duty_u16(potentiometer.read_u16()) #matches the potentiometer input to PWM output for the led
	#Note: duty (specified 0-100) is how many pulses are active per cycle (which is determined by frequency)

	print(voltage)
	utime.sleep_ms(100)