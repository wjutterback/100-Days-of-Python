print('Welcome to the tip calculator.')
bill_total = float(input('What was the total bill? $'))
percentage_tip = input('What percentage tip would you like to give? 10, 12, or 15?')
bill_split = input('How many people to split the bill?')

bill = round(bill_total * (1 + int(percentage_tip)/100) / int(bill_split), 2)
print(f'Each person should pay: {bill}')