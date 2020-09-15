#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import libraries
import sqlite3

# design a schema for policyholders
conn = sqlite3.connect('policyholders.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS policyholder (
                            identifier VARCHAR(36) PRIMARY KEY,
                            gender VARCHAR(255),
                            date_of_birth DATE,
                            SSN VARCHAR(255)
                            )''')

c.execute('''CREATE TABLE IF NOT EXISTS medical_conditions (
                            user_id PRIMARY KEY,
                            smoking_status VARCHAR(255),
                            allergies VARCHAR(255),
                            medical_conditions VARCHAR(255),
                            FOREIGN KEY (user_id) REFERENCES policyholder(identifier)
                            )''')


c.execute('''CREATE TABLE IF NOT EXISTS insured_events (
                            event_id integer PRIMARY KEY AUTOINCREMENT,
                            user_id VARCHAR(36),
                            loss_date DATE,
                            type_of_issue VARCHAR(255),
                            billed_amount DOUBLE,
                            covered_amount DOUBLE,
                            FOREIGN KEY (user_id) REFERENCES policyholder(identifier)
                            )''')

