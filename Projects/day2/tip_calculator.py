print('Welcome to the tip calculator.')
bill_total = float(input('What was the total bill? $'))
percentage_tip = input('What percentage tip would you like to give? 10, 12, or 15?')
bill_split = input('How many people to split the bill?')

bill = bill_total * (1 + int(percentage_tip)/100) / int(bill_split)
formatted_bill = "{:.2f}".format(bill)
print(f'Each person should pay: ${formatted_bill}')