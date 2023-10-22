'''
@author Yuri Nunes

Week 07 Project: Windchill Calculator
'''

# Windchill Formula
# W = 35.74 + (0.6215 * T) - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)

def calculate_windchill(temperature, windspeed):
    WINDSPEED_CONSTANT = windspeed ** 0.16
    windchill = 35.74 + (0.6215 * temperature) - (35.75 * WINDSPEED_CONSTANT) + (0.4275 * temperature * WINDSPEED_CONSTANT)
    return windchill

def celsius_to_fahrenheit(celsius_temperature):
    CONVERTION_CONSTANT = (9/5)
    fahrenheit_temperature = (celsius_temperature * CONVERTION_CONSTANT) + 32
    return fahrenheit_temperature

# Main Program
unparsed_temperature = float(input('> What is the temperature? '))
temperature_unity = input('> Fahrenheit or Celsius (F/C)? ').upper()
temperature = unparsed_temperature if temperature_unity == 'F' else celsius_to_fahrenheit(unparsed_temperature)

for windspeed in range(5, 65, 5):
    windchill = calculate_windchill(temperature, windspeed)
    print(f'At temperature {temperature:.1f}F, and wind speed {windspeed} mph, the windchill is: {windchill:.2f}F')