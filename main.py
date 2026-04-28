from services.account_service import *
from utils.file_handler import *
from utils.analytics import *
accounts.extend(load_accounts())
while True:
    print("1.Create 2.Deposit 3.Withdraw 4.Analytics 5.Save 6.Exit")
    ch = int(input())
    if ch == 1:
        create_account()
    elif ch == 2:
        deposit()
    elif ch == 3:
        withdraw()
    elif ch == 4:
        run_analytics(accounts, transactions)
    elif ch == 5:
        save_accounts(accounts)
    elif ch == 6:
        break
