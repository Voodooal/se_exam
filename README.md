# se_exam
## Working code
The working code for the software exam can be found in policyholder.py.

## Design a schema for policyholders
The schema designed can be found in schema.py.

## Design a data structure for aggregate metrics
```python
agg_metrics = {'Total Covered Amount':0,'Claims per year':0,'Avg age':0}
agg_metrics['Total Covered Amount'] = insured_events.total_covered_amount()
agg_metrics['Claims per year'] = insured_events.claim_per_year()
agg_metrics['Avg age'] = policyholder.avg_age()
```

## Methods
### Adds an insured individual and returns the unique identifier of that individual
```python
@classmethod
def add_policyholder(cls,gender,date_of_birth,SSN):
  policyholder = cls(gender,date_of_birth,SSN)
  return str(policyholder.identifier)
```

### Adds an insurance event for a specific user identified by unique identifier
```python
@classmethod
def add_insured_events(cls,user_id,loss_date,type_of_issue,billed_amount,covered_amount):
  return cls(user_id,loss_date,type_of_issue,billed_amount,covered_amount) 
```

### List all insured individuals
```python
def print_policyholders():
  for ins in policyholder.policyholders:
    print (ins.identifier, ins.gender, ins.date_of_birth)
```

### List all events associated with a specific user by unique identifier
```python
@classmethod
def print_event_for_user(cls,user_id):
  for event in insured_events.events:
    if event.user_id == user_id:
        print(event.events_id,event.user_id,event.loss_date,
              event.type_of_issue,event.billed_amount,
              event.covered_amount)
```

## What considerations should you take into account when using or storing information such as Social Security Numbers?
When using sensitive information such as Social Security Number, we need to make sure that it doesn't show in cleartext and only part of the data can be seen. When storing such information, we need to encrypt the data instead of storing the raw data in the database. We also need to set means of authentications, such as password, for the person to access the data.  
Other than paying extra attention and putting more restrictions on the access of the sensitive data, we should also eliminate the unnecessary storage or usage of these information. For example, we could use the unique identifier we generated to identify the user rather than using their SSN. 
