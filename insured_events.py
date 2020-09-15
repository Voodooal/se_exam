#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
import uuid


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