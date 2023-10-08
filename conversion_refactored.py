import conversions
import test

miles = 5
yards = 2000
meters = 1205.12
fromUnit = miles
toUnit =[yards,meters]
value = fromUnit

def convert(fromUnit, toUnit, value):
    fromUnit = miles
    toUnit = [yards, meters]
    value = fromUnit

    for unit in toUnit:
        new_value = value * unit
        print(new_value)
    return new_value
