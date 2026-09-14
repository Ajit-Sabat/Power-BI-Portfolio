import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(100)

OUTPUT_DIR = Path(__file__).parent.parent / "data" / "incremental_01"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NUM_NEW_CUSTOMERS = 15
NUM_UPDATED_CUSTOMERS = 5
NUM_ACCOUNTS = 25
NUM_TRANSACTIONS = 50
NUM_NEW_LOANS = 5
NUM_UPDATED_LOANS = 3
NUM_PAYMENTS = 10

FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Rahul",
    "Rohan", "Karan", "Neha", "Priya", "Ananya"
]

LAST_NAMES = [
    "Sharma", "Patel", "Mehta", "Shah", "Joshi",
    "Kumar", "Singh", "Desai", "Gupta", "Nair"
]

CITIES = [
    ("Mumbai", "WEST"),
    ("Pune", "WEST"),
    ("Delhi", "NORTH"),
    ("Bangalore", "SOUTH"),
    ("Chennai", "SOUTH")
]

ACCOUNT_TYPES = {
    "SAVINGS": "P001",
    "CURRENT": "P002",
    "SALARY": "P003"
}

TRANSACTION_TYPES = [
    "DEPOSIT",
    "WITHDRAWAL",
    "TRANSFER",
    "PAYMENT"
]

CHANNELS = [
    "ATM",
    "ONLINE",
    "BRANCH",
    "MOBILE"
]

LOAN_TYPES = [
    "HOME",
    "PERSONAL",
    "AUTO",
    "EDUCATION"
]


def write_csv(filename, rows, fieldnames):
    filepath = OUTPUT_DIR / filename

    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Created: {filepath}")


# =========================================================
# 1. CUSTOMERS
# =========================================================

new_customers = []

for i in range(121, 121 + NUM_NEW_CUSTOMERS):
    city, region = random.choice(CITIES)

    new_customers.append({
        "customer_id": f"C{i:03d}",
        "first_name": random.choice(FIRST_NAMES),
        "last_name": random.choice(LAST_NAMES),
        "gender": random.choice(["MALE", "FEMALE"]),
        "date_of_birth": date(
            random.randint(1970, 2000),
            random.randint(1, 12),
            random.randint(1, 28)
        ),
        "city": city,
        "region": region,
        "customer_segment": random.choice([
            "RETAIL",
            "PREMIUM",
            "SALARY"
        ]),
        "customer_status": "ACTIVE"
    })


# Existing customers C001-C005 are updated.
updated_customers = []

for i in range(1, 1 + NUM_UPDATED_CUSTOMERS):
    city, region = random.choice(CITIES)

    updated_customers.append({
        "customer_id": f"C{i:03d}",
        "first_name": random.choice(FIRST_NAMES),
        "last_name": random.choice(LAST_NAMES),
        "gender": random.choice(["MALE", "FEMALE"]),
        "date_of_birth": date(
            random.randint(1970, 2000),
            random.randint(1, 12),
            random.randint(1, 28)
        ),
        "city": city,
        "region": region,
        "customer_segment": random.choice([
            "RETAIL",
            "PREMIUM",
            "SALARY"
        ]),
        "customer_status": random.choice([
            "ACTIVE",
            "ACTIVE",
            "INACTIVE"
        ])
    })

customer_rows = new_customers + updated_customers

write_csv(
    "customers_incremental_01.csv",
    customer_rows,
    [
        "customer_id",
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "city",
        "region",
        "customer_segment",
        "customer_status"
    ]
)


# =========================================================
# 2. ACCOUNTS
# =========================================================

accounts = []

customer_pool = new_customers + [
    {"customer_id": f"C{i:03d}"}
    for i in range(1, 6)
]

for i in range(121, 121 + NUM_ACCOUNTS):
    customer = random.choice(customer_pool)
    account_type = random.choice(list(ACCOUNT_TYPES.keys()))

    accounts.append({
        "account_id": f"A{i:03d}",
        "customer_id": customer["customer_id"],
        "product_id": ACCOUNT_TYPES[account_type],
        "account_type": account_type,
        "account_status": "ACTIVE",
        "open_date": date(
            2026,
            random.randint(1, 9),
            random.randint(1, 28)
        )
    })

write_csv(
    "accounts_incremental_01.csv",
    accounts,
    [
        "account_id",
        "customer_id",
        "product_id",
        "account_type",
        "account_status",
        "open_date"
    ]
)


# =========================================================
# 3. TRANSACTIONS
# =========================================================

transactions = []

for i in range(101, 101 + NUM_TRANSACTIONS):
    account = random.choice(accounts)

    transactions.append({
        "transaction_id": f"T{i:03d}",
        "account_id": account["account_id"],
        "customer_id": account["customer_id"],
        "transaction_date": date(
            2026,
            random.randint(8, 9),
            random.randint(1, 14)
        ),
        "transaction_type": random.choice(TRANSACTION_TYPES),
        "transaction_amount": round(
            random.uniform(500, 50000), 2
        ),
        "transaction_channel": random.choice(CHANNELS),
        "transaction_status": random.choice([
            "SUCCESS",
            "SUCCESS",
            "SUCCESS",
            "FAILED"
        ])
    })

write_csv(
    "transactions_incremental_01.csv",
    transactions,
    [
        "transaction_id",
        "account_id",
        "customer_id",
        "transaction_date",
        "transaction_type",
        "transaction_amount",
        "transaction_channel",
        "transaction_status"
    ]
)


# =========================================================
# 4. LOANS
# =========================================================

new_loans = []

loan_customer_pool = new_customers + [
    {"customer_id": f"C{i:03d}"}
    for i in range(1, 6)
]

for i in range(16, 16 + NUM_NEW_LOANS):
    customer = random.choice(loan_customer_pool)

    start_date = date(
        2026,
        random.randint(1, 8),
        random.randint(1, 28)
    )

    maturity_date = start_date + timedelta(days=365 * 5)

    loan_amount = round(
        random.uniform(100000, 1000000), 2
    )

    outstanding_amount = round(
        loan_amount * random.uniform(0.5, 0.95), 2
    )

    new_loans.append({
        "loan_id": f"L{i:03d}",
        "customer_id": customer["customer_id"],
        "loan_type": random.choice(LOAN_TYPES),
        "loan_amount": loan_amount,
        "interest_rate": round(
            random.uniform(7, 14), 2
        ),
        "start_date": start_date,
        "maturity_date": maturity_date,
        "loan_status": "ACTIVE",
        "outstanding_amount": outstanding_amount
    })


# Existing loans L001-L003 are updated.
updated_loans = []

for i in range(1, 1 + NUM_UPDATED_LOANS):
    updated_loans.append({
        "loan_id": f"L{i:03d}",
        "customer_id": f"C{i:03d}",
        "loan_type": random.choice(LOAN_TYPES),
        "loan_amount": round(
            random.uniform(100000, 1000000), 2
        ),
        "interest_rate": round(
            random.uniform(7, 14), 2
        ),
        "start_date": date(
            2026,
            random.randint(1, 8),
            random.randint(1, 28)
        ),
        "maturity_date": date(2031, 12, 31),
        "loan_status": random.choice([
            "ACTIVE",
            "ACTIVE",
            "CLOSED"
        ]),
        "outstanding_amount": round(
            random.uniform(10000, 500000), 2
        )
    })

loan_rows = new_loans + updated_loans

write_csv(
    "loans_incremental_01.csv",
    loan_rows,
    [
        "loan_id",
        "customer_id",
        "loan_type",
        "loan_amount",
        "interest_rate",
        "start_date",
        "maturity_date",
        "loan_status",
        "outstanding_amount"
    ]
)


# =========================================================
# 5. LOAN PAYMENTS
# =========================================================

payments = []

for i in range(31, 31 + NUM_PAYMENTS):
    loan = random.choice(new_loans)

    payment_amount = round(
        random.uniform(5000, 50000), 2
    )

    principal_amount = round(
        payment_amount * 0.8, 2
    )

    interest_amount = round(
        payment_amount - principal_amount, 2
    )

    payments.append({
        "payment_id": f"P{i:03d}",
        "loan_id": loan["loan_id"],
        "customer_id": loan["customer_id"],
        "payment_date": date(
            2026,
            random.randint(8, 9),
            random.randint(1, 14)
        ),
        "payment_amount": payment_amount,
        "principal_amount": principal_amount,
        "interest_amount": interest_amount,
        "payment_status": "SUCCESS"
    })

write_csv(
    "loan_payments_incremental_01.csv",
    payments,
    [
        "payment_id",
        "loan_id",
        "customer_id",
        "payment_date",
        "payment_amount",
        "principal_amount",
        "interest_amount",
        "payment_status"
    ]
)


# =========================================================
# SUMMARY
# =========================================================

print("\nIncremental Batch 01 generated successfully.")
print(f"New customers: {len(new_customers)}")
print(f"Updated customers: {len(updated_customers)}")
print(f"New accounts: {len(accounts)}")
print(f"New transactions: {len(transactions)}")
print(f"New loans: {len(new_loans)}")
print(f"Updated loans: {len(updated_loans)}")
print(f"New loan payments: {len(payments)}")