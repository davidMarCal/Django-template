from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#Manager class to set the model
class PersonManager(models.Manager):
    def create_person(self,first_name,last_name,user):
        person=self.create(first_name=first_name,last_name=last_name,user=user)
        return person

    def update_person(self,first_name,last_name,user):
        person=self.update(first_name=first_name,last_name=last_name,user=user)
        return person

    def get_person(self,user):
        person=Person.objects.get(user=user)
        return person
    
    def delete_Persons(self):
        persons=Person.objects.all()
        persons.delete()

class Person(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    

    objects=PersonManager()

    #The above Person model would create a database table like this:

    #CREATE TABLE myapp_person (
    #    "id" serial NOT NULL PRIMARY KEY,
    #    "first_name" varchar(30) NOT NULL,
    #    "last_name" varchar(30) NOT NULL
    #);
