from django.db import models

# Create your models here.

'''
 why the django give you the model field:
     1 - html idget
     2 - validation
     3- db size 
'''      
JOB_TYPE = (('full_time','Full_time'),
            ('part_time','Part_time'))
class Job(models.Model): # table 
    title = models.CharField(max_length=100) #column
    # job_type
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    # description
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)


    def __str__(self):
          return self.title
     
