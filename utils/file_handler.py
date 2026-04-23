import csv
from datetime import datetime

def save_accounts(accounts):
    with open("data/accounts.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["AccNo", "Name", "Type", "Balance", "Timestamp"])
        for acc in accounts:
            writer.writerow([acc["acc_no"], acc["name"], acc["type"], acc["balance"], acc["time"]])

def load_accounts():
    accounts = []
    try:
        with open("data/accounts.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                accounts.append({
                    "acc_no": int(row["AccNo"]),
                    "name": row["Name"],
                    "type": row["Type"],
                    "balance": float(row["Balance"]),
                    "time": datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S.%f")
                })
    except:
        print("No file found")
    return accounts