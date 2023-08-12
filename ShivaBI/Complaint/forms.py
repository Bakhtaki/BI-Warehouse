from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django_jalali.forms import jDateField
from django_jalali.admin.widgets import AdminjDateWidget
from django.forms.widgets import PasswordInput, TextInput
from . models import Complaint


# User Registration.
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# Login Form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={
        'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        label=("Password"), strip=False, widget=PasswordInput(attrs={
            'autocomplete': 'current-password', 'class': 'form-control'}))


# Create Complaint Form
class CreateComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = [
            'customer_name', 'customer_family', 'customer_phone',
            'Province', 'City', 'customer_address', 'Persian_year',
            'Persian_month', 'Persian_day', 'customer_type', 'accepted',
            'complaint_category', 'external_material',
            'complaint_description', 'product_category', 'product_code',
            'product_name', 'product_price', 'product_barcode',
            'quantity', 'Persian_production_year',
            'Persian_production_month', 'Persian_production_day',
            'production_site', 'production_shift', 'complaint_status',
            'action', 'action_description', 'action_date'
        ]


# Update Complaint Form
class UpdateComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = [
            'customer_name', 'customer_family', 'customer_phone',
            'Province', 'City', 'customer_address', 'Persian_year',
            'Persian_month', 'Persian_day', 'customer_type', 'accepted',
            'complaint_category', 'external_material',
            'complaint_description', 'product_category', 'product_code',
            'product_name', 'product_price', 'product_barcode',
            'quantity', 'Persian_production_year',
            'Persian_production_month', 'Persian_production_day',
            'production_site', 'production_shift', 'complaint_status',
            'action', 'action_description', 'action_date'
        ]
