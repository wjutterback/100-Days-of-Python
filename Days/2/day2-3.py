# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
inputYears = int(age)
years_remaining = 90 - inputYears

calculatedDay = years_remaining * 365
calculatedWeeks = years_remaining * 52
calculatedMonths = years_remaining * 12

print(f"You have {calculatedDay} days, {calculatedWeeks} weeks, and {calculatedMonths} months left.")