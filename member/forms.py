from django import forms

from .models import Student

class Empforms(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"