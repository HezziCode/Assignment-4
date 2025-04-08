user_input = int(input("Enter the temperature in Fahrenheit: "))
degrees_celsius = (user_input - 32) * 5.0 / 9.0
rounded_value = round(degrees_celsius, 2)
print(f"Temperature: {user_input}°F = {rounded_value}°C")
