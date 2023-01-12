def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Ingresa tu peso en kilogramos: "))
height = float(input("Ingresa tu altura en metros: "))

bmi = calculate_bmi(weight, height)

if bmi < 18.5:
    print("Bajo peso")
elif 18.5 <= bmi < 25:
    print("Peso normal")
elif 25 <= bmi < 30:
    print("Sobrepeso")
else:
    print("Obesidad")

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Ingresa tu peso en kilogramos: "))
height = float(input("Ingresa tu altura en metros: "))

bmi = calculate_bmi(weight, height)
print("Tu índice de masa corporal es: ", bmi)