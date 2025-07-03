-- Create database and table for Bank Management System

CREATE DATABASE IF NOT EXISTS bank_db;

USE bank_db;

CREATE TABLE IF NOT EXISTS accounts (
    account_number VARCHAR(10) PRIMARY KEY,
    account_holder VARCHAR(100),
    balance DOUBLE DEFAULT 0
);
