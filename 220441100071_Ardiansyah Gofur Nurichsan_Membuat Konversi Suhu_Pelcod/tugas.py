print("Konversi Suhu")
print("Awalan\n1. Celcius\n2. Fahrenheit\n3. Kelvin\n4. Reamur\n5. Rankine")
pilih = int(input("Suhu Awal: "))
print("Akhiran\n1. Celcius\n2. Fahrenheit\n3. Kelvin\n4. Reamur\n5. Rankine")
akhir = int(input("Suhu Akhir; "))

nilai = int(input("Besaran Suhu; "))

if pilih==1:
    Fahrenheit = nilai*9/5+32
    Kelvin = nilai+273.15
    Reamur = nilai*4/5
    Rankine = (nilai+273.15)*9/5
    Celcius = nilai
elif pilih==2:
    Celcius = (nilai-32)*5/9
    Kelvin = (nilai+459.67)*5/9
    Reamur = (nilai-32)*4/9
    Rankine = nilai+459.67
    Fahrenheit = nilai
elif pilih==3:
    Celcius = nilai-273.15
    Fahrenheit = (nilai*9/5)-459.67
    Reamur = (nilai-273)*4/5
    Rankine = nilai*9/5
    Kelvin = nilai
elif pilih==4:
    Celcius = nilai/0.8
    Fahrenheit = (nilai*2.25)+32
    Kelvin = (nilai/0.8)+273.15
    Rankine = (nilai*2.25)+491.67
    Reamur = nilai
else:
    Celcius = (nilai-491.67)*5/9
    Fahrenheit = nilai-459.67
    Kelvin = nilai*5/9
    Reamur = (nilai/1.8+273.15)*0.8
    Rankine = nilai

if akhir==1:
    print(Celcius)
elif akhir==2:
    print(Fahrenheit)
elif akhir==3:
    print(Kelvin)
elif akhir==4:
    print(Reamur)
else:
    print(Rankine)

