import machine
import utime
import urandom

led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

pressed = False
timer_start = utime.ticks_ms()

# handler for interrupt
def button_handler(pin):
    global pressed
    if not pressed:
        pressed = True # ignores other button presses
        timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
        print("Your reaction time was " + str(timer_reaction) + " miliseconds!")

led.value(1)
utime.sleep(urandom.uniform(5,10)) # pause between 5 and 10 seconds
led.value(0)
button.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler) # interrupt