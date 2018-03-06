# Write your code here :-)
# CircuitPlaygroundExpress_Temperature
# reads the on-board temperature sensor and prints the value
 
import adafruit_thermistor
import digitalio
import board
import time
import neopixel

 
thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)

tempUp = digitalio.DigitalInOut(board.BUTTON_A)
tempUp.direction = digitalio.Direction.INPUT 
tempUp.pull = digitalio.Pull.DOWN
tempDown = digitalio.DigitalInOut(board.BUTTON_B)
tempDown.direction = digitalio.Direction.INPUT
tempDown.pull = digitalio.Pull.DOWN

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.show()




def wheel(pixelCount):
    color = (0, 0, 0)
    
    if pixelCount == 1:
        color = (0x10, 0, 0x10)
    elif pixelCount == 2:
        color = (0x10, 0, 0x10)
    elif pixelCount == 3:
        color = (0, 0, 0x10)
    elif pixelCount == 4:
        color = (0, 0x10, 0)
    elif pixelCount == 5:
        color = (0, 0x10, 0)
    elif pixelCount == 6:
        color = (0x10, 0x10, 0)
    elif pixelCount == 7:
        color = (0x10, 0x10, 0)
    elif pixelCount == 8:
        color = (0x10, 0, 0)
    elif pixelCount == 9:
        color = (0x10, 0, 0)
    elif pixelCount == 10:
        color = (0x10, 0, 0)
        
    for i in range(pixelCount):
        pixels[i] = color
    for i in range(pixelCount, 10, 1):
        pixels[i] = (0, 0, 0)

tuningFactor = 0.5
center = 23
spread = 1

while True:
    if tempUp.value:
        center = center + 1
    if tempDown.value:
        center = center - 1
        
    if(abs(thermistor.temperature-center-4*spread) < tuningFactor):
        wheel(1)
    if(abs(thermistor.temperature-center-3*spread) < tuningFactor):
        wheel(2)
    if(abs(thermistor.temperature-center-2*spread) < tuningFactor):
        wheel(3)
    if(abs(thermistor.temperature-center-spread) < tuningFactor):
        wheel(4)
    if(abs(thermistor.temperature-center) < tuningFactor):
        wheel(5)
    if(abs(thermistor.temperature-center+spread) < tuningFactor):
        wheel(6)
    if(abs(thermistor.temperature-center+2*spread) < tuningFactor):
        wheel(7)
    if(abs(thermistor.temperature-center+3*spread) < tuningFactor):
        wheel(8)
    if(abs(thermistor.temperature-center+4*spread) < tuningFactor):
        wheel(9)
    if(abs(thermistor.temperature-center+5*spread) < tuningFactor):
        wheel(10)
    pixels.show

    print(thermistor.temperature)
    time.sleep(0.1)
