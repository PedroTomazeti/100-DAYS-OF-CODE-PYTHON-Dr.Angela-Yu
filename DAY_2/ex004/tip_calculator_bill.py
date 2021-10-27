print('Welcome to the tip calculator!')
TotalBill = float(input('What was the total bill? $'))
PctTip = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
TotalPP = int(input('How many people to split the bill? '))
PayTotal = (TotalBill * (1 + (PctTip/100)))/TotalPP
print(f'Each person should pay: ${round(PayTotal,2)}')
