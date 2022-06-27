# Entrada do número desejado, ressaltando que deve ser um número inteiro
number = int(input("Which number do you want to check? "))

# Será analisado o resto da divisão entre o número inserido e o número 2, caso seja 0 é porque ele é par, caso contrário ele é ímpar.
if number % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")
