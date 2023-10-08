import conversions
import conversion_refactored
import unittest

class TestKel(unittest.TestCase)
    cel =(300, 572, 573.15)
    far =(300, 572, 573.15)
    kel =(300, 572, 573.15)

    def test_cel_temp(self):
        for celsius in self.cel:
            cel_kelTemp = conversions.convertCelsiusToKelvin(celsius)
            cel_farTemp = conversions.convertCelsiusToFahrenheit(celsius)

    def test_far_temp(self):
        for fahrenheit in self.far:
            far_celTemp = conversions.convertFahrenheitToCelsius(fahrenheit)
            far_kelTemp = conversions.convertFahrenheitToKelvin(fahrenheit)

    def test_kel_temp(self):
        for kelvin in self.kel:
            kel_celTemp = conversions.convertKelvinToCelsius(kelvin)
            kel_kelTemp = conversions.convertKelvinToFahrenheit(kelvin)

class TestMile(unittest.TestCase):
    fromUnit = (35, 50, 95)
    toUnit = (2000, 1205.12)
    value = fromUnit

    def test_mile_conv(self):
        for fromUnit, toUnit, value in self.fromUnit, self.toUnit, self.value:
            mile_conv = conversion_refactored.convert(fromUnit,toUnit, value)

if __name__ == '__main__':
    unittest.main()
