class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        # Convert Celsius to Fahrenheit
        return (celsius * 9/5) + 32


# Calling the static method without creating an object
temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)

print(f"{temp_c}°C is equal to {temp_f}°F")
