# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
inputYears = int(age)
years_remaining = 90 - inputYears

calculated_day = years_remaining * 365
calculated_weeks = years_remaining * 52
calculated_months = years_remaining * 12

print(f"You have {calculated_day} days, {calculated_weeks} weeks, and {calculated_months} months left.")