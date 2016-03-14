from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.note)
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    priority = models.IntegerField(default=1)
    assignment = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
 

 
