import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)

def pir_handler(pin): #code that runs on interrupt
    utime.sleep_ms(100) #prevent pir from being triggered by jitter in signal (debouncing)
    if pin.value():
        print("ALARM! Motion Detected!")
        for i in range(50): #flash the led and buzz buzzer 50 times
            led.toggle()
            buzzer.toggle()
            utime.sleep_ms(100)

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler) #interrupt (irq)

while True: #always running unless interrupted
    led.toggle()
    utime.sleep(5)