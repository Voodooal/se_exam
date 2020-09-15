#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime,date
import uuid
import pytest

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
        

class medical_conditions:
    
    instances = []
    def __init__(self, user_id, smoking_status, allergies, medical_conditions):
        self.user_id = user_id
        self.smoking_status = smoking_status
        self.allergies = allergies
        self.medical_conditions = medical_conditions
        medical_conditions.instances.append(self)

# Add medical conditions for a specific user by unique identifier     
    @classmethod
    def add_medical_conditions(cls,user_id, smoking_status, allergies, medical_conditions):
        return cls(user_id, smoking_status, allergies, medical_conditions)


class insured_events:
    
    events = []
    def __init__(self,user_id,loss_date,type_of_issue,billed_amount,covered_amount):
        self.events_id = str(uuid.uuid4())
        self.user_id = user_id
        self.loss_date = datetime.strptime(loss_date, '%m/%d/%Y')
        self.type_of_issue = type_of_issue
        self.billed_amount = billed_amount
        self.covered_amount = covered_amount
        insured_events.events.append(self)
    

# Adds an insurance event for a specific user identified by unique identifier    
    @classmethod
    def add_insured_events(cls,user_id,loss_date,type_of_issue,billed_amount,covered_amount):
        return cls(user_id,loss_date,type_of_issue,billed_amount,covered_amount)    

# List all events associated with a specific user by unique identifie    
    @classmethod
    def print_event_for_user(cls,user_id):
        for event in insured_events.events:
            if event.user_id == user_id:
                print(event.events_id,event.user_id,event.loss_date,
                      event.type_of_issue,event.billed_amount,
                      event.covered_amount)

# Calculate the total covered amount     
    def total_covered_amount():
        total_covered_amount = 0
        for event in insured_events.events:
            total_covered_amount += event.covered_amount
        return total_covered_amount

# Calculate the claims per year    
    def claim_per_year():
        claim_per_year = {}
        for event in insured_events.events:
            year = str(event.loss_date.year)
            if year not in claim_per_year.keys():
                claim_per_year[year] = 1
            else:
                claim_per_year[year] += 1
        return claim_per_year
    
# test cases
policyholder.add_policyholder('female','08/08/1998','xxx-xxx-1234')
policyholder.add_policyholder('male','08/09/1998','xxx-xxx-5678')
policyholder.add_policyholder('male','09/10/1968','xxx-xxx-5678')
#policyholder.print_policyholders()

insured_events.add_insured_events(policyholder.policyholders[0].identifier,'08/15/2020','WC',100,100)
insured_events.add_insured_events(policyholder.policyholders[1].identifier,'01/15/2018','Auto',5000,4500)
insured_events.add_insured_events(policyholder.policyholders[2].identifier,'08/30/2018','Auto',10000,10000)
#insured_events.print_event_for_user(policyholder.policyholders[0].identifier)    


# data structure for aggregate metrics
agg_metrics = {'Total Covered Amount':0,'Claims per year':0,'Avg age':0}
agg_metrics['Total Covered Amount'] = insured_events.total_covered_amount()
agg_metrics['Claims per year'] = insured_events.claim_per_year()
agg_metrics['Avg age'] = policyholder.avg_age()


def test_total_covered_amount():
    assert agg_metrics['Total Covered Amount'] == 14600


def test_claims_per_year():
    assert agg_metrics['Claims per year'] == {'2020':1,'2018':2}


def test_avg_age():
    assert agg_metrics['Avg age'] == 32.0


