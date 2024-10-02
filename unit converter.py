# Unit Converter Program

def length_converter(value, from_unit, to_unit):
    length_units = {
        'meter': 1,
        'kilometer': 0.001,
        'centimeter': 100,
        'millimeter': 1000,
        'mile': 0.000621371,
        'yard': 1.09361,
        'foot': 3.28084,
        'inch': 39.3701
    }
    
    if from_unit in length_units and to_unit in length_units:
        return value * (length_units[to_unit] / length_units[from_unit])
    else:
        return "Invalid length unit!"

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'kilogram': 1,
        'gram': 1000,
        'milligram': 1_000_000,
        'pound': 2.20462,
        'ounce': 35.274
    }
    
    if from_unit in weight_units and to_unit in weight_units:
        return value * (weight_units[to_unit] / weight_units[from_unit])
    else:
        return "Invalid weight unit!"

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return "Invalid temperature unit!"

# Main Program
print("Unit Converter")
print("1. Length")
print("2. Weight")
print("3. Temperature")

choice = input("Select the type of conversion (1/2/3): ")

if choice == '1':
    value = float(input("Enter the value to convert: "))
    from_unit = input("Enter the unit you're converting from (meter, kilometer, centimeter, etc.): ").lower()
    to_unit = input("Enter the unit you're converting to: ").lower()
    result = length_converter(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")

elif choice == '2':
    value = float(input("Enter the value to convert: "))
    from_unit = input("Enter the unit you're converting from (kilogram, gram, pound, etc.): ").lower()
    to_unit = input("Enter the unit you're converting to: ").lower()
    result = weight_converter(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")

elif choice == '3':
    value = float(input("Enter the temperature value to convert: "))
    from_unit = input("Enter the unit you're converting from (celsius, fahrenheit, kelvin): ").lower()
    to_unit = input("Enter the unit you're converting to: ").lower()
    result = temperature_converter(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")

else:
    print("Invalid choice!")
