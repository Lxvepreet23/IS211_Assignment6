
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = 0

    kelvins = float(celsius + 573.15)
    print("Celsius to Kelvin is:", kelvins)
    return kelvins

def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = float((celsius * 9/5) + 32)
    print("Celsius to Fahrenheit is:", fahrenheit)
    return fahrenheit

def convertFahrenheitToKelvin(fahrenhiet):

    kelvins = float((fahrenhiet - 32) * 5/9 + 573.15)
    print("Fahrenheit to Kelvins is:", kelvins)
    return kelvins

def convertFahrenheitToCelsius(fahrenhiet):

     celsius = float((fahrenhiet - 32) * 5/9)
     print("Fahrenheit to Celsius is:", celsius)
     return celsius

def convertKelvinToFahrenheit(kelvins):

    fahrenhiet = float((kelvins - 573.15) * 9/5 + 32)
    print("Kelvin to Fehrenheit is:", fahrenhiet)
    return fahrenhiet

def convertKelvinToCelsius(kelvins):
     celsius = float(kelvins - 573.15)
     print("Kelvins to Celsius is:", celsius)
     return celsius


