# Get detials of loan
money_owed = float(input('How much money do you owe, in dollars?\n')) # $50,000

apr = float(input('What is the annual percentage rate?\n')) # 3%

payment = float(input('What is the monthly payment you can make?\n')) # $1000

months = int(input('How many months do you want to see results for?\n')) # 24

monthly_rate = apr/100/12

# Calculate interest to pay
interest_paid = money_owed * monthly_rate

# Add in interest
money_owed = money_owed + interest_paid

# Make monthly payment
money_owed = money_owed - payment

print('Paid', payment, 'of which', interest_paid, 'was interest', 'Now Owed', money_owed)