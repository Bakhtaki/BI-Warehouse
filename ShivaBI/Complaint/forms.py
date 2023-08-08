from django import forms
from django_jalali.forms import jDateField
from . import models


class Create_ComplaintForm(forms.Form):
    # positive integer field
    id = forms.IntegerField()
    complaint_date_persian = jDateField()
    complaint_date = forms.DateField()
    channel = forms.ChoiceField(choices=models.Complaint.channel_choices)
