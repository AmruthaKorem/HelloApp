balance = int(input())
n = int(input())

for i in range(n):
    operation, amount = input().split()
    amount = int(amount)

    if operation == "Deposit":
        balance += amount
    elif operation == "Withdraw":
        if balance >= amount:
            balance -= amount

print(balance)
