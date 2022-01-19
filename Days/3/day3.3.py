# 🚨 Don't change the code below 👇
height = input("enter your height in inches: ")
weight = input("enter your weight in lbs: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weightNum = int(weight)
heightNum = int(height)
BMI = weightNum/heightNum**2 * 703
roundedBMI = int(BMI)

if roundedBMI < 18.5:
  print(f'Your BMI is {roundedBMI}. You are underweight.')
elif roundedBMI < 25:
  print(f'Your BMI is {roundedBMI}. You are a normal weight.')
elif roundedBMI < 30:
  print(f'Your BMI is {roundedBMI}. You are overweight.')
elif roundedBMI < 35:
  print(f'Your BMI is {roundedBMI}. You are obese.')
elif roundedBMI >= 35:
  print(f'Your BMI is {roundedBMI}. You are clinically obese.')