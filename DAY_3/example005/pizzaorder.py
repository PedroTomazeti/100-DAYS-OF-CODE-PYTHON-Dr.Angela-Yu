print("Welcome to Python Pizza Deliveries!")

print("Small Pizza is $15.")
print("Medium Pizza is $20.")
print("Large Pizza is $25.")

size = input("What size pizza do you want (S, M, or L)? ")
bill = 0

if size.upper() == "S":
    bill = 15
elif size.upper() == "M":
    bill = 20
else:
    bill = 25

print("Pepperoni for Small Pizza: +$2")
print("Pepperoni for Medium or Large Pizza: +$3")
add_pepperoni = input("Do you want pepperoni (Y/N)? ")
if add_pepperoni.upper() == "Y":
    if size.upper() == "S":
        bill+=2
    else:
        bill+=3

print("Extra cheese for any size pizza: +$1")
extra_cheese = input("Do you want extra cheese (Y/N)? ")
if extra_cheese.upper() == "Y":
    bill+=1

print(f"Your final bill is: ${bill}.")
