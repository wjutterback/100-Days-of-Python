# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
inputYears = int(age)
expectedDays = 365 * 90
expectedWeeks = 52 * 90
expectedMonths = 12 * 90

currentDays = inputYears * 365
currentWeeks = inputYears * 52
currentMonths = inputYears * 12

calculatedDay = expectedDays - currentDays
calculatedWeeks = expectedWeeks - currentWeeks
calculatedMonths = expectedMonths - currentMonths

print(f"You have {calculatedDay} days, {calculatedWeeks} weeks, and {calculatedMonths} months left.")