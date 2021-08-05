from w1thermsensor import W1ThermSensor, Unit
import time

sensor = W1ThermSensor()

while True:
    temperature_in_celsius = sensor.get_temperature()
    temperature_in_fahrenheit = sensor.get_temperature(Unit.DEGREES_F)
    print("celsius:    {0:.3f}".format(temperature_in_celsius))
    print("fahrenheit: {0:.3f}".format(temperature_in_fahrenheit))

    time.sleep(5.0)
