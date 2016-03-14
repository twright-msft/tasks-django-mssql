from django.shortcuts import render
from tasksapp.models import Person, Task
from rest_framework import viewsets
from tasksapp.serializers import PersonSerializer, TaskSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Persons to be viewed or edited.
    """
    queryset = Person.objects.all().order_by('id')
    serializer_class = PersonSerializer
    
class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer