# project 8 is a temerature converter
# it uses basic concepts of functions and modular programming
#it converts temperatures between Celsius, Fahrenheit, and Kelvin

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, from_unit, to_unit):
    if (from_unit) == 'C':
        if (to_unit) == 'F':
            return celsius_to_fahrenheit(value)
        elif (to_unit) == 'K':
            return celsius_to_kelvin(value)
    elif (from_unit) == 'F':
        if (to_unit) == 'C':
            return fahrenheit_to_celsius(value)
        elif (to_unit) == 'K':
            return fahrenheit_to_kelvin(value)
    elif (from_unit) == 'K':
        if (to_unit) == 'C':
            return kelvin_to_celsius(value)
        elif (to_unit) == 'F':
            return kelvin_to_fahrenheit(value)
    return None

while True:
    print("Welcome to the Temperature Converter!")
    print("Available units: C (Celsius), F (Fahrenheit), K (Kelvin)")
    from_unit = input("Enter the unit you are converting from (or 'quit' to exit): ").upper()
    if from_unit == 'QUIT':
        break
    to_unit = input("Enter the unit you are converting to: ").upper()
    try:
        value = float(input(f"Enter the temperature value in {from_unit}: "))
    except ValueError:
        print("Invalid temperature value, please try again.")
        continue
    result = convert_temperature(value, from_unit, to_unit)
    if result is not None:
        print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
    else:
        print("Invalid conversion units, please try again.")