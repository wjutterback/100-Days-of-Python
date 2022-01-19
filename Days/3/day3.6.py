# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true = ['t', 'r', 'u', 'e']
love = ['l', 'o', 'v', 'e']

true_counter = 0
love_counter = 0

for i in name1:
  for x in true:
    if (i == x):
      true_counter += 1

for i in name2:
  for x in true:
    if (i == x):
      true_counter += 1

for i in name1:
  for x in love:
    if (i == x):
      love_counter += 1

for i in name2:
  for x in love:
    if (i==x):
      love_counter += 1

if (true_counter >= 10):
  true_counter = 9
if (love_counter >= 10):
  love_counter = 9

if (true_counter <= 1 or true_counter >= 9):
  print(f'Your score is {true_counter}{love_counter}, you go together like coke and mentos')
elif(true_counter >= 4 and true_counter <= 5):
  print(f'Your score is {true_counter}{love_counter}, you are alright together')
else:
  print(f'Your score is {true_counter}{love_counter}')