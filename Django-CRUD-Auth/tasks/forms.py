from django.forms import ModelForm
from .models import Task

#here you can crete yours forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']