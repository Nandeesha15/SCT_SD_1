def celsius_to_others(temp):
    fahrenheit = (temp * 9 / 5) + 32
    kelvin = temp + 273.15
    print(f"\nCelsius: {temp:.2f}\nFahrenheit: {fahrenheit:.2f}\nKelvin: {kelvin:.2f}")

def fahrenheit_to_others(temp):
    celsius = (temp - 32) * 5 / 9
    kelvin = celsius + 273.15
    print(f"\nFahrenheit: {temp:.2f}\nCelsius: {celsius:.2f}\nKelvin: {kelvin:.2f}")

def kelvin_to_others(temp):
    if temp < 0:
        print("\nInvalid temperature! Kelvin cannot be less than 0.")
        return
    celsius = temp - 273.15
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"\nKelvin: {temp:.2f}\nCelsius: {celsius:.2f}\nFahrenheit: {fahrenheit:.2f}")

def main():
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")

    try:
        choice = int(input("Enter your choice (1-3): "))
        if choice not in [1, 2, 3]:
            print("Invalid choice! Please select between 1 and 3.")
            return

        temp = float(input("Enter the temperature to convert: "))

        if choice == 1:
            celsius_to_others(temp)
        elif choice == 2:
            fahrenheit_to_others(temp)
        elif choice == 3:
            kelvin_to_others(temp)
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
