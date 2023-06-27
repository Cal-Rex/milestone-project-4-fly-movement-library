# imports the Item class from the local models.py file
from .models import UserOneRepMax
# imports the forms library from django
from django import forms


# class calls on the Modelform class inside the forms library from django
class OneRmForm(forms.ModelForm):
    # class meta used here to establish the metadata of the form element
    class Meta:
        # the model is the imported Item model from models.py
        model = UserOneRepMax
        # then the fields are listed as a python list of strings
        # that match the variable names
        fields = ('one_rep_max',)
