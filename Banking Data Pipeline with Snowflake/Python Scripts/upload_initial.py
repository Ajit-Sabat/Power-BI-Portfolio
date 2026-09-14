import snowflake.connector
from pathlib import Path


# =========================
# CONFIGURATION
# =========================

ACCOUNT = "GE26397.central-india.azure"
USER = "AJITSABAT23"
PASSWORD = "AjitS@8956613801"
WAREHOUSE = "COMPUTE_WH"
DATABASE = "BANKING_DWH"
SCHEMA = "BRONZE"
ROLE = "ACCOUNTADMIN"

STAGE = "@BANKING_DWH.BRONZE.BANKING_STAGE"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "initial"


FILES = [
    "customers_initial.csv",
    "accounts_initial.csv",
    "transactions_initial.csv",
    "loans_initial.csv",
    "loan_payments_initial.csv"
]


# =========================
# CONNECT TO SNOWFLAKE
# =========================

conn = snowflake.connector.connect(
    account="GE26397.central-india.azure",
    user=USER,
    password=PASSWORD,
    warehouse="COMPUTE_WH",
    database="BANKING_DWH",
    schema="BRONZE",
    role="ACCOUNTADMIN"
)

cursor = conn.cursor()


# =========================
# UPLOAD FILES
# =========================

try:

    for filename in FILES:

        file_path = DATA_DIR / filename

        if not file_path.exists():
            print(f"ERROR: File not found → {file_path}")
            continue

        # Convert Windows path to Snowflake-compatible path
        snowflake_path = file_path.as_posix()

        sql = f"""
        PUT 'file://{snowflake_path}'
        {STAGE}
        AUTO_COMPRESS = FALSE
        OVERWRITE = FALSE;
        """

        print(f"\nUploading: {filename}")

        result = cursor.execute(sql)

        for row in result:
            print(row)

    print("\nAll initial files processed.")


finally:

    cursor.close()
    conn.close()