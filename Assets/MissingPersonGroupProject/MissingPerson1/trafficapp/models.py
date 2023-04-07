from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    date_missing = models.DateField(default=datetime.today, blank=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    age_at_missing = models.IntegerField(default=0)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    gender = models.CharField(max_length=100)    
    race = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return (self.full_name)
    
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    #override the save method
    def save(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(Person, self).save() # Call the "real" save() method.                                
