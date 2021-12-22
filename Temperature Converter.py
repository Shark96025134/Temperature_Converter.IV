print("Temperature Converter")
a = int(input("Enter The Temperature here:" ))
print("1.Celsius")
print("2.Fahrenheit")
print("3.Kelvin")
s = input("Enter the Initial Scale here:")
b = input("Enter the Scale into which you want to convert the Temperature:" )
c=a*9/5+32
d=(a-32)*5/9
e= a + 273.15
f= a - 273.15
g= (a + 459.67)*5/9
h= a * 9/5 - 459.67
if s== "Celsius" and b == "Fahrenheit":
    print (c,"℉")

if s== "Fahrenheit" and b == "Celsius":
    print (d,"°C")

if s== "Kelvin" and b == "Celsius":
    print (f,"°C")

if s== "Celsius" and b == "Kelvin":
    print (e,"°K")

if s== "Fahrenheit" and b == "Kelvin":
    print (g,"°K")

if s== "Kelvin" and b == "Farhenheit":
    print (h,"°F")
