print("Welcome to the rollercoaster!")
# entrada da altura
height = int(input("What is your height in cm? "))

# Realiza a análise da altura em cm, se ela for maior ou igual a 120cm será permitido, caso contrário não poderá.
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    # Depois de analisada a altura, terá o parâmetro idade para poder ser realizado o pagamento de acordo com ela.
    if age < 12:
        print("Please pay $5.")
    elif age > 18:
        print("Please pay 12$.")
    else:
        print("Please pay $7.")
else:
    print("Sorry, you have to grow taller before you can ride.")
