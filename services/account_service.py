from datetime import datetime
from utils.validators import *

accounts = []
transactions = []

def create_account():
    try:
        acc_no = int(input("Acc no: "))
        validate_account_number(acc_no)

        name = input("Name: ")
        acc_type = input("Type: ")
        balance = float(input("Balance: "))
        validate_amount(balance)

        acc = {
            "acc_no": acc_no,
            "name": name,
            "type": acc_type,
            "balance": balance,
            "time": datetime.now()
        }

        accounts.append(acc)
        transactions.append((acc_no, "Created", balance, datetime.now()))

    except Exception as e:
        print("Error:", e)

def deposit():
    acc_no = int(input("Acc no: "))
    amt = float(input("Amount: "))
    for acc in accounts:
        if acc["acc_no"] == acc_no:
            acc["balance"] += amt

def withdraw():
    try:
        acc_no = int(input("Acc no: "))
        amt = float(input("Amount: "))

        for acc in accounts:
            if acc["acc_no"] == acc_no:
                validate_withdraw(acc["balance"], amt)
                acc["balance"] -= amt

    except Exception as e:
        print(e)