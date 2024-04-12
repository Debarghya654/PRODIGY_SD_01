# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:42:57 2024

@author: Debarghya Das
"""

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

def convert_temperature(temp, unit):
    if unit.lower() == 'c':
        celsius = temp
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{temp} Celsius is equal to:")
        print(f"{fahrenheit:.2f} Fahrenheit")
        print(f"{kelvin:.2f} Kelvin")
    elif unit.lower() == 'f':
        fahrenheit = temp
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{temp} Fahrenheit is equal to:")
        print(f"{celsius:.2f} Celsius")
        print(f"{kelvin:.2f} Kelvin")
    elif unit.lower() == 'k':
        kelvin = temp
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{temp} Kelvin is equal to:")
        print(f"{celsius:.2f} Celsius")
        print(f"{fahrenheit:.2f} Fahrenheit")
    else:
        print("Invalid unit entered!")
        return

def main():
    print("\033[H\033[2J")
    print("====================================================")
    print("\t\t\t Temperature Conversion \t\t\t")
    print("====================================================")
    print("C for Celsius")
    print("F for Fahrenheit")
    print("K for Kelvin")
    temp = float(input("Enter the Temperature Value: "))
    unit = input("Enter the Original Unit of Measurement (C/F/K): ")
    convert_temperature(temp, unit)

if __name__ == "__main__":
    main()
