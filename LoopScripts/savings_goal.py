# Define known values
bank_bal = 452
savings_goal = 1500
weekly_savings = 112

# Calculate the unknown
while bank_bal < savings_goal:
    bank_bal += weekly_savings
    print(f'This week my balance increased to {round(bank_bal, 2)}')
    if bank_bal >= savings_goal:
        print(f'Goal met! My current balance is {round(bank_bal, 2)}')
        break
    if bank_bal >= (savings_goal * .75):
        bank_bal -= (bank_bal * .05)
        print(f'So close! After treating myself, my balance is up to {round(bank_bal, 2)}')
    elif bank_bal > (savings_goal * .5):
         print(f'Almost there! This week my balance is up to {round(bank_bal, 2)}')