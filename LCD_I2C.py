import machine

sda = machine.Pin(0) # data channel wire
scl = machine.Pin(1) # clock wire
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

# sending data:
# Note: 114 refers to the address of the screen and \x indicates a hexadecimal string
i2c.writeto(114, '\x7C') # 7C enters command mode
i2c.writeto(114, '\x2D') # 2D clears the screen and resets the cursor to the beginning
i2c.writeto(114, "  IT is life!!!") #prints to the screen!