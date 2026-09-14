import os
from pathlib import Path
import snowflake.connector

conn = snowflake.connector.connect(
    user="AJITSABAT23",
    account="GE26397.central-india.azure",
    password="AjitS@8956613801",
    warehouse="COMPUTE_WH",
    database="BANKING_DWH",
    schema="BRONZE"
)

cursor = conn.cursor()

files = [
    "customers_incremental_02.csv",
    "accounts_incremental_02.csv",
    "transactions_incremental_02.csv",
    "loans_incremental_02.csv",
    "loan_payments_incremental_02.csv"
]

local_dir = Path(__file__).parent.parent / "data" / "incremental_02"

for file_name in files:
    file_path = local_dir / file_name
    file_uri = file_path.as_posix()

    cursor.execute(
        f"PUT 'file://{file_uri}' "
        f"@BANKING_DWH.BRONZE.BANKING_STAGE "
        f"AUTO_COMPRESS=FALSE OVERWRITE=FALSE"
    )

    print(f"Uploaded: {file_name}")

cursor.close()
conn.close()

print("Incremental batch upload completed.")