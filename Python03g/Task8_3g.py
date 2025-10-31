#Task 8: ATM Simulator
balance = 1000
choice = 0

while choice != 4:
    print('''
ATM Menu:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
''')
    choice = int(input("Choice: "))

    #if statements for choices

    if choice == 1: print(f'Your balance: ${balance:.2f}')

    if choice == 2:
        depos = int(input("Deposit amount: $"))
        balance += depos
        print(f'New balance: ${balance:.2f}')

    if choice == 3:
        withdraw = int(input("Withdraw amount: $"))
        if withdraw > balance:
            print(f'Insufficient Balance. Balance is currently ${balance:.2f}')
            withdraw = int(input("Withdraw amount: $"))
        
        balance -= withdraw
        print(f'New balance: ${balance:.2f}')

print('Have a good day!')
