"""
Parâmetros para o cálculo do IMC.
- Abaixo de 18,5 estão abaixo do peso
- Acima de 18,5, mas abaixo de 25 eles têm um peso normal
- Acima de 25 anos, mas abaixo de 30, eles estão um pouco acima do peso
- Acima de 30, mas abaixo de 35 eles são obesos
- Acima de 35 são clinicamente obesos.
"""
# Entra com a altura em metros e o peso em quilogramas.
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight/pow(height, 2))
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")
