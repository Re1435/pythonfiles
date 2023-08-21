t = input()
temp = t[-1]
value = t[:-1]
if temp == "C":
    cel_val = float(value)
    celcius = str(float(cel_val))+temp
    print(celcius)
    fahrenit = str(float((cel_val * 1.8) + 32))+"F"
    print(fahrenit)
    kelvin = str(float(cel_val+273))+"K"
    print(kelvin)
elif temp == "F":
    fahren_val = float(value)
    celcius = str(round(((fahren_val-32)*5)/9, 2))+"C"
    print(celcius)
    fahrenit = str(float(fahren_val))+"F"
    print(fahrenit)
    kelvin = str(float(celcius[:-1])+273)+"K"
    print(kelvin)
else:
    kelvin_val = float(value)
    celcius = str(kelvin_val - 273)+"C"
    print(celcius)
    fahrenit = str(round(1.8*float(celcius[:-1])+32, 2))+"F"
    print(fahrenit)
    kelvin = str(float(kelvin_val))+"K"
    print(kelvin)
