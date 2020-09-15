#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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