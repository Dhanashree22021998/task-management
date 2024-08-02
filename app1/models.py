from django.db import models

choice_status=[
    ('Onboarded','Onboarded'),
    ('Not Onboarded','Not Onboarded')
]

choice_domain= [
    ('SAAS','SAAS'),
    ('Ecommerce','Ecommerce'),
    ('CRM','CRM'),
    ('ERP','ERP'),
    ('Finance','Finance')
]
class Employee(models.Model):


    eid= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    department = models.CharField(max_length = 50)
    date_of_joining = models.DateTimeField()
    status = models.CharField(max_length=45,choices=choice_status)
    project_domain =models.CharField(max_length=25,choices=choice_domain)
