import csv
import random
from datetime import date, datetime, timedelta
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

SEED = 42

NUM_CUSTOMERS = 100
NUM_ACCOUNTS = 120
NUM_TRANSACTIONS = 100
NUM_LOANS = 15

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data" / "initial"

random.seed(SEED)


# ============================================================
# REFERENCE DATA
# ============================================================

FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Rahul",
    "Rohan", "Karan", "Vikram", "Amit", "Nikhil",
    "Ananya", "Priya", "Neha", "Pooja", "Sneha",
    "Riya", "Kavya", "Isha", "Meera", "Aisha"
]

LAST_NAMES = [
    "Sharma", "Patel", "Mehta", "Shah", "Desai",
    "Joshi", "Verma", "Kapoor", "Gupta", "Nair",
    "Iyer", "Rao", "Singh", "Malhotra", "Kulkarni"
]

CITIES = {
    "Mumbai": "West",
    "Pune": "West",
    "Ahmedabad": "West",
    "Delhi": "North",
    "Jaipur": "North",
    "Lucknow": "North",
    "Bengaluru": "South",
    "Chennai": "South",
    "Hyderabad": "South",
    "Kochi": "South"
}

ACCOUNT_TYPES = [
    "SAVINGS",
    "CURRENT",
    "SALARY"
]

PRODUCTS = {
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

TRANSACTION_CHANNELS = [
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

LOAN_STATUSES = [
    "ACTIVE",
    "CLOSED"
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def random_date(start_date, end_date):
    days = (end_date - start_date).days
    return start_date + timedelta(days=random.randint(0, days))


def write_csv(filename, data):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    file_path = OUTPUT_DIR / filename

    if not data:
        print(f"Created {file_path} -> 0 records")
        return

    fieldnames = list(data[0].keys())

    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Created {file_path} -> {len(data)} records")


# ============================================================
# CUSTOMER GENERATION
# ============================================================

def generate_customers():
    customers = []

    for i in range(1, NUM_CUSTOMERS + 1):

        customer_id = f"C{i:04d}"

        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)

        city = random.choice(list(CITIES.keys()))
        region = CITIES[city]

        gender = random.choice(["M", "F"])

        dob = random_date(
            date(1960, 1, 1),
            date(2000, 12, 31)
        )

        segment = random.choice([
            "STANDARD",
            "PREMIUM",
            "VIP"
        ])

        status = random.choice([
            "ACTIVE",
            "ACTIVE",
            "ACTIVE",
            "INACTIVE"
        ])

        customers.append({
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "date_of_birth": dob.isoformat(),
            "city": city,
            "region": region,
            "customer_segment": segment,
            "customer_status": status
        })

    return customers


# ============================================================
# ACCOUNT GENERATION
# ============================================================

def generate_accounts(customers):
    accounts = []

    for i in range(1, NUM_ACCOUNTS + 1):

        account_id = f"A{i:05d}"

        customer = random.choice(customers)

        account_type = random.choice(ACCOUNT_TYPES)

        open_date = random_date(
            date(2020, 1, 1),
            date(2025, 12, 31)
        )

        status = random.choice([
            "ACTIVE",
            "ACTIVE",
            "ACTIVE",
            "CLOSED"
        ])

        accounts.append({
            "account_id": account_id,
            "customer_id": customer["customer_id"],
            "product_id": PRODUCTS[account_type],
            "account_type": account_type,
            "account_status": status,
            "open_date": open_date.isoformat()
        })

    return accounts


# ============================================================
# TRANSACTION GENERATION
# ============================================================

def generate_transactions(accounts):
    transactions = []

    for i in range(1, NUM_TRANSACTIONS + 1):

        transaction_id = f"T{i:06d}"

        account = random.choice(accounts)

        transaction_type = random.choice(TRANSACTION_TYPES)

        transaction_date = random_date(
            date(2025, 1, 1),
            date(2026, 8, 31)
        )

        amount = round(
            random.uniform(500, 100000),
            2
        )

        transactions.append({
            "transaction_id": transaction_id,
            "account_id": account["account_id"],
            "customer_id": account["customer_id"],
            "transaction_date": transaction_date.isoformat(),
            "transaction_type": transaction_type,
            "transaction_amount": amount,
            "transaction_channel": random.choice(
                TRANSACTION_CHANNELS
            ),
            "transaction_status": "COMPLETED"
        })

    return transactions


# ============================================================
# LOAN GENERATION
# ============================================================

def generate_loans(customers):
    loans = []

    for i in range(1, NUM_LOANS + 1):

        loan_id = f"L{i:05d}"

        customer = random.choice(customers)

        loan_type = random.choice(LOAN_TYPES)

        loan_amount = round(
            random.uniform(100000, 2000000),
            2
        )

        interest_rate = round(
            random.uniform(7.0, 14.0),
            2
        )

        start_date = random_date(
            date(2022, 1, 1),
            date(2025, 12, 31)
        )

        maturity_date = start_date + timedelta(
            days=random.choice([
                365,
                730,
                1095,
                1825,
                3650
            ])
        )

        status = random.choice(LOAN_STATUSES)

        outstanding_amount = round(
            loan_amount * random.uniform(0.2, 0.9),
            2
        )

        if status == "CLOSED":
            outstanding_amount = 0.0

        loans.append({
            "loan_id": loan_id,
            "customer_id": customer["customer_id"],
            "loan_type": loan_type,
            "loan_amount": loan_amount,
            "interest_rate": interest_rate,
            "start_date": start_date.isoformat(),
            "maturity_date": maturity_date.isoformat(),
            "loan_status": status,
            "outstanding_amount": outstanding_amount
        })

    return loans


# ============================================================
# LOAN PAYMENT GENERATION
# ============================================================

def generate_loan_payments(loans):
    payments = []

    payment_counter = 1

    for loan in loans:

        num_payments = random.randint(1, 3)

        for _ in range(num_payments):

            payment_id = f"LP{payment_counter:06d}"

            payment_counter += 1

            payment_date = random_date(
                date(2025, 1, 1),
                date(2026, 8, 31)
            )

            payment_amount = round(
                random.uniform(5000, 50000),
                2
            )

            principal_amount = round(
                payment_amount * random.uniform(0.7, 0.9),
                2
            )

            interest_amount = round(
                payment_amount - principal_amount,
                2
            )

            payment_status = random.choice([
                "PAID",
                "PAID",
                "LATE",
                "MISSED"
            ])

            payments.append({
                "payment_id": payment_id,
                "loan_id": loan["loan_id"],
                "customer_id": loan["customer_id"],
                "payment_date": payment_date.isoformat(),
                "payment_amount": payment_amount,
                "principal_amount": principal_amount,
                "interest_amount": interest_amount,
                "payment_status": payment_status
            })

    return payments


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 60)
    print("BANKING DATA GENERATOR")
    print("=" * 60)

    customers = generate_customers()

    accounts = generate_accounts(customers)

    transactions = generate_transactions(accounts)

    loans = generate_loans(customers)

    loan_payments = generate_loan_payments(loans)

    write_csv(
        "customers_initial.csv",
        customers
    )

    write_csv(
        "accounts_initial.csv",
        accounts
    )

    write_csv(
        "transactions_initial.csv",
        transactions
    )

    write_csv(
        "loans_initial.csv",
        loans
    )

    write_csv(
        "loan_payments_initial.csv",
        loan_payments
    )

    print("\nGeneration complete.")
    print(f"Customers      : {len(customers)}")
    print(f"Accounts       : {len(accounts)}")
    print(f"Transactions   : {len(transactions)}")
    print(f"Loans          : {len(loans)}")
    print(f"Loan Payments  : {len(loan_payments)}")


if __name__ == "__main__":
    main()