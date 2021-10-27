age = input("What is your current age? ")
CurrentAge = int(age)
DaysRemaining = (90*365) - CurrentAge*365
WeeksRemaining = (90*52) - CurrentAge*52
MonthsRemaining = (90*12) - CurrentAge*12
print(f'You have {DaysRemaining} Days, {WeeksRemaining} weeks, {MonthsRemaining} months left.')
