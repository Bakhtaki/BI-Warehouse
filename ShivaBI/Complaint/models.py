from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import post_save
from django_jalali.db.models import jDateField


# Create your models here

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organizer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Complaint(models.Model):
    # ID of the complaint
    id = models.AutoField(primary_key=True)
    # Agent
    agent = models.ForeignKey(
        'Agent', on_delete=models.SET_NULL, null=True, blank=True)
    # Organizer
    organizer = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    # Persian date field
    complaint_date_persian = jDateField()
    # Contact Type field
    contact_type = models.ForeignKey(
        "ContactType", on_delete=models.CASCADE, default=1)
    # Customer Type field
    customer_type = models.ForeignKey(
        "CustomerType", on_delete=models.CASCADE, null=True, blank=True)
    # Customer Name field
    Customer_name = models.CharField(max_length=100, blank=True, null=True)
    # Customer Phone field
    Customer_phone = models.CharField(max_length=100, blank=True, null=True)
    # Production Date
    production_date_persian = jDateField()
    # Acceptance Status
    acceptance_status = models.BooleanField(
        default=True, null=True, blank=True)
    # Complaints Title
    complaint_title = models.CharField(max_length=100)
    # Complaint Category
    complaint_category = models.ForeignKey(
        "ComplaintCategory", on_delete=models.CASCADE, default=1)
    # Complaint SubCategory
    complaint_subcategory = models.ForeignKey(
        "ComplaintSubCategory",
        on_delete=models.CASCADE,
        blank=True, null=True)
    # External Material
    external_material = models.ForeignKey(
        "ExternalMaterial", on_delete=models.CASCADE, null=True, blank=True)
    # Product Category
    product_category = models.ForeignKey(
        "ProductCategory", on_delete=models.CASCADE)
    # Product Code
    product_code = models.ForeignKey("Product",
                                     on_delete=models.CASCADE)
    # Product Batch exactly 13 characters
    product_batch = models.CharField(max_length=13, blank=True, null=True)
    # Complaint Quantity
    complaint_quantity = models.IntegerField(null=True, blank=True, default=1)
    # Production Shift
    production_shift = models.ForeignKey(
        "ShiftModel",
        on_delete=models.CASCADE, blank=True, null=True, default=1)
    # Production Site
    production_site = models.ForeignKey(
        "ProductionSite", on_delete=models.CASCADE,
        null=True, blank=True, default=1)
    # Send Gift
    send_gift = models.BooleanField(default=False, blank=True, null=True)
    # Gift
    gift = models.ForeignKey(
        "GiftModel", on_delete=models.CASCADE, null=True, blank=True)
    # Complaint Description
    complaint_description = models.TextField(
        max_length=1000, blank=True, null=True)


# Contact Type Model
class ContactType(models.Model):
    id = models.AutoField(primary_key=True)
    contact_type = models.CharField(max_length=100)

    def __str__(self):
        return self.contact_type


# Customer Type Model
class CustomerType(models.Model):
    id = models.AutoField(primary_key=True)
    customer_type = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_type


# Complaint Category Model
class ComplaintCategory(models.Model):
    id = models.AutoField(primary_key=True)
    complaint_category = models.CharField(max_length=100)

    def __str__(self):
        return self.complaint_category


# Complaint SubCategory Model
class ComplaintSubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    compliant_category = models.ForeignKey(
        "ComplaintCategory", on_delete=models.CASCADE)
    complaint_subcategory = models.CharField(max_length=100)

    def __str__(self):
        return self.complaint_subcategory


# External Material Model
class ExternalMaterial(models.Model):
    id = models.AutoField(primary_key=True)
    external_material = models.CharField(max_length=100)

    def __str__(self):
        return self.external_material


# Product Category Model
class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    product_category = models.CharField(max_length=100)

    def __str__(self):
        return self.product_category


# Product Model
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=100)
    product_category = models.ForeignKey(
        "ProductCategory", on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


# Shift Model
class ShiftModel(models.Model):
    id = models.AutoField(primary_key=True)
    shift = models.CharField(max_length=100)

    def __str__(self):
        return self.shift


# Production Site Model
class ProductionSite(models.Model):
    id = models.AutoField(primary_key=True)
    production_site = models.CharField(max_length=100)

    def __str__(self):
        return self.production_site


# GiftModel
class GiftModel(models.Model):
    id = models.AutoField(primary_key=True)
    gift_type = models.CharField(max_length=100)
    gift_name = models.CharField(max_length=100)

    def __str__(self):
        return self.gift_type


# Complaint Actions Model
class ComplaintAction(models.Model):
    id = models.AutoField(primary_key=True)
    complaint = models.ForeignKey("Complaint", on_delete=models.CASCADE)
    action_date_persian = jDateField()
    action_description = models.TextField(max_length=1000)
    action_status = models.BooleanField(default=True)
    action_result = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return super().__str__()


# User Creation Signal
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Post Notification
post_save.connect(create_user_profile, sender=User)
