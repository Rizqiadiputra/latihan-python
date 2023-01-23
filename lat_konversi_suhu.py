print("\n PROGRAM KONVERSI TEMPERATUR \n")

celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah", celcius, "Celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur", reamur, "Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit", fahrenheit, "Fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin", kelvin, "Kelvin")