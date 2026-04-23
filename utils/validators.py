def validate_account_number(acc_no):
    if acc_no <= 0:
        raise ValueError("Invalid account number")

def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

def validate_withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")