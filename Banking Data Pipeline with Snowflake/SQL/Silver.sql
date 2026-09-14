USE DATABASE BANKING_DWH;
USE SCHEMA SILVER;

DROP TABLE IF EXISTS SILVER_CUSTOMER;
DROP TABLE IF EXISTS SILVER_ACCOUNT;
DROP TABLE IF EXISTS SILVER_TRANSACTION;
DROP TABLE IF EXISTS SILVER_LOAN;
DROP TABLE IF EXISTS SILVER_LOAN_PAYMENT;


CREATE TABLE SILVER_CUSTOMER AS
SELECT
    TRIM(customer_id) AS customer_id,
    TRIM(first_name) AS first_name,
    TRIM(last_name) AS last_name,
    UPPER(TRIM(gender)) AS gender,
    date_of_birth,
    TRIM(city) AS city,
    TRIM(region) AS region,
    UPPER(TRIM(customer_segment)) AS customer_segment,
    UPPER(TRIM(customer_status)) AS customer_status
FROM BANKING_DWH.BRONZE.BRONZE_CUSTOMER;


CREATE TABLE SILVER_ACCOUNT AS
SELECT
    TRIM(account_id) AS account_id,
    TRIM(customer_id) AS customer_id,
    TRIM(product_id) AS product_id,
    UPPER(TRIM(account_type)) AS account_type,
    UPPER(TRIM(account_status)) AS account_status,
    open_date
FROM BANKING_DWH.BRONZE.BRONZE_ACCOUNT;


CREATE TABLE SILVER_TRANSACTION AS
SELECT
    TRIM(transaction_id) AS transaction_id,
    TRIM(account_id) AS account_id,
    TRIM(customer_id) AS customer_id,
    transaction_date,
    UPPER(TRIM(transaction_type)) AS transaction_type,
    transaction_amount,
    UPPER(TRIM(transaction_channel)) AS transaction_channel,
    UPPER(TRIM(transaction_status)) AS transaction_status
FROM BANKING_DWH.BRONZE.BRONZE_TRANSACTION;


CREATE TABLE SILVER_LOAN AS
SELECT
    TRIM(loan_id) AS loan_id,
    TRIM(customer_id) AS customer_id,
    UPPER(TRIM(loan_type)) AS loan_type,
    loan_amount,
    interest_rate,
    start_date,
    maturity_date,
    UPPER(TRIM(loan_status)) AS loan_status,
    outstanding_amount
FROM BANKING_DWH.BRONZE.BRONZE_LOAN;


CREATE TABLE SILVER_LOAN_PAYMENT AS
SELECT
    TRIM(payment_id) AS payment_id,
    TRIM(loan_id) AS loan_id,
    TRIM(customer_id) AS customer_id,
    payment_date,
    payment_amount,
    principal_amount,
    interest_amount,
    UPPER(TRIM(payment_status)) AS payment_status
FROM BANKING_DWH.BRONZE.BRONZE_LOAN_PAYMENT;


SHOW TABLES;
SELECT * FROM BANKING_DWH.SILVER.SILVER_TRANSACTION;


SELECT 'CUSTOMER' AS TABLE_NAME, COUNT(*) AS ROW_COUNT FROM SILVER_CUSTOMER
UNION ALL
SELECT 'ACCOUNT', COUNT(*) FROM SILVER_ACCOUNT
UNION ALL
SELECT 'LOAN', COUNT(*) FROM SILVER_LOAN
UNION ALL
SELECT 'LOAN_PAYMENT', COUNT(*) FROM SILVER_LOAN_PAYMENT
UNION ALL
SELECT 'TRANSACTION', COUNT(*) FROM SILVER_TRANSACTION;


