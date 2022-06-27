print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

points_true_1 = name1.lower().count("t") + name1.lower().count("r") + name1.lower().count("u") + name1.lower().count("e")
points_true_2 = name2.lower().count("t") + name2.lower().count("r") + name2.lower().count("u") + name2.lower().count("e")
ptt = (points_true_1 + points_true_2) * 10

points_love_1 = name1.lower().count("l") + name1.lower().count("o") + name1.lower().count("v") + name1.lower().count("e")
points_love_2 = name2.lower().count("l") + name2.lower().count("o") + name2.lower().count("v") + name2.lower().count("e")
plt = points_love_1 + points_love_2

total = ptt + plt

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
