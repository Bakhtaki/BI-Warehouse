from django import forms
from django.contrib.auth import get_user_model
from django_jalali.forms import jDateField
from django_jalali.admin.widgets import AdminjDateWidget
from django.contrib.auth.forms import UserCreationForm, UsernameField
from . import models

User = get_user_model()


class Create_ComplaintForm(forms.Form):
    # positive integer fieldUsernameField
    id = forms.IntegerField()
    # Persian date field
    complaint_date_persian = jDateField(widget=AdminjDateWidget)
    # Load Complaint Type Values from ComplaintType Model
    contact_type = forms.ModelChoiceField(
        queryset=models.ContactType.objects.all())
    # Load Customer Type Values from CustomerType Model
    customer_type = forms.ModelChoiceField(
        queryset=models.CustomerType.objects.all())
    # Customer Name
    Customer_name = forms.CharField(max_length=100)
    # Customer Phone
    Customer_phone = forms.CharField(max_length=100)
    # Production Date
    production_date_persian = jDateField(widget=AdminjDateWidget)
    # Acceptance Status
    acceptance_status = forms.BooleanField()
    # Complaints Title
    complaint_title = forms.CharField(max_length=100)
    # Load Complaint Category Values from ComplaintCategory Model
    complaint_category = forms.ModelChoiceField(
        queryset=models.ComplaintCategory.objects.all())
    # Load Complaint SubCategory Values from ComplaintSubCategory Model
    complaint_subcategory = forms.ModelChoiceField(
        queryset=models.ComplaintSubCategory.objects.all())
    # Load External Material Values from ExternalMaterial Model
    external_material = forms.ModelChoiceField(
        queryset=models.ExternalMaterial.objects.all())
    # Load Product Category Values from ProductCategory Model
    product_category = forms.ModelChoiceField(
        queryset=models.ProductCategory.objects.all())
    # Load products where the product category is a product category
    product_code = forms.ModelChoiceField(
        queryset=models.Product.objects.all())
    # Product Batch exactly 13 characters
    product_batch = forms.CharField(max_length=13)
    # Complaint Quantity
    complaint_quantity = forms.IntegerField()
    # Product Shift
    ProductionShift = forms.ModelChoiceField(
        queryset=models.ShiftModel.objects.all())
    # Production Site
    ProductionSite = forms.ModelChoiceField(
        queryset=models.ProductionSite.objects.all())
    # Send Gift
    send_gift = forms.BooleanField()
    # Gift
    gift = forms.ModelChoiceField(queryset=models.GiftModel.objects.all())
    # Description
    description = forms.CharField(max_length=1000)


# Custom User Creation Form
class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = User
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}


# Product Category Update Form
class ProductCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = models.ProductCategory
        fields = ('product_category',)
