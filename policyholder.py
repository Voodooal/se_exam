#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime,date
import uuid


class policyholder:
    
    policyholders = []
    def __init__(self, gender, date_of_birth, SSN):
        self.identifier = str(uuid.uuid4())
        self.gender = gender
        self.date_of_birth = datetime.strptime(date_of_birth, '%m/%d/%Y')
        self.SSN = SSN
        policyholder.policyholders.append(self)

# Adds an insured individual and returns the unique identifier of that individual    
    @classmethod
    def add_policyholder(cls,gender,date_of_birth,SSN):
        policyholder = cls(gender,date_of_birth,SSN)
        return str(policyholder.identifier)

# List all insured individuals    
    def print_policyholders():
        for ins in policyholder.policyholders:
            print (ins.identifier, ins.gender, ins.date_of_birth)

# Calculate the average age for all users    
    def avg_age():
        age_dict = {'age':0,'count':0}
        
        for x in policyholder.policyholders:
            age = date.today().year - x.date_of_birth.year
            age_dict['age'] += age
            age_dict['count'] += 1
        
        return age_dict['age']/age_dict['count']
        
