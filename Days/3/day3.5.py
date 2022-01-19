# 🚨 Don't change the code below 👇
from audioop import add


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()
# 🚨 Don't change the code above 👆
print(size, add_pepperoni, extra_cheese)
#Write your code below this line 👇

bill = 0
if size == 's':
  bill += 15
elif size == 'm':
  bill += 20
else:
  bill += 25

if add_pepperoni == 'y' and size =='s':
  bill += 2
elif add_pepperoni == 'y':
  bill += 3

if extra_cheese == 'y':
  bill += 1

print(f'You bill is {bill}')