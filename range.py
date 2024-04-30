total = 0
expeneses = []
num_expenses = int(input('Enter number of expenses: '))

for i in range(num_expenses): # or could be range(int)
    expeneses.append(float(input('Enter an expense: ')))

total = sum(expeneses)

print('Your total expense is $', total, sep='')