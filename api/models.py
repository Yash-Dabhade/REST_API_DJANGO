from django.db import models

# Company Model
class Company(models.Model):
    #auto field 
    company_id=models.AutoField(primary_key=True)

    #normal fields
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=100)
    about=models.TextField()

    #pass with tuples
    type=models.CharField(max_length=100,choices=(('IT','Information_Technology'),('Non IT','Non Information Technology'),('MP','Mobile Phones')))

    #log
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    # To view name of model instead of object
    def __str__(self):
        return self.name


# Employee Model
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(('MN','Manager'),('SDE','Software Developer'),('PL','Project Leader'),('MG','Manager'),('AS','Assistant')))

    #Foreign Key  (One to Many Relationship)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)

    # To view name of model instead of object
    def __str__(self):
        return self.name