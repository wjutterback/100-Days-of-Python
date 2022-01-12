# 🚨 Don't change the code below 👇
height = input("enter your height in inches: ")
weight = input("enter your weight in lbs: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weightNum = int(weight)
heightNum = int(height)
BMI = weightNum/heightNum**2 * 703
roundedBMI = round(BMI, 2)
print(roundedBMI)