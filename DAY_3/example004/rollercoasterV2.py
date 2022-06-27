print("Welcome to the rollercoaster!")
# entrada da altura
height = int(input("What is your height in cm? "))
bill = 0


# Realiza a análise da altura em cm, se ela for maior ou igual a 120cm será permitido, caso contrário não poderá.
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    # Depois de analisada a altura, terá o parâmetro idade para poder ser realizado o pagamento de acordo com ela.
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age > 18:
        if age >= 45 and age <= 55:
            print("Your entry is free.")
        else:
            bill = 12
            print("Adult tickets are $12.")
    else:
        bill = 7
        print("Youth tickets are $7.")

    print("A photo costs $3.")
    wants_photo = input("Do you want a photo taken (Y/N)? ")
    if wants_photo.upper() == "Y":
        #Adiciona $3 para a conta
        bill+=3
    
    print(f"Your total bill is: ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
