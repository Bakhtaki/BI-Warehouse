from django.db import models
from django_jalali.db.models import jDateField


# Create your models here
class Complaint(models.Model):
    id = models.AutoField(primary_key=True)
    # Persian date field
    complaint_date_persian = jDateField()
    # Complaint date field
    complaint_date = models.DateField()
    # Complaint channel
    channel_choices = (
        (0, "Phone"),
        (1, "Social Media"),
        (2, "Distribution Company"),
        (3, "Website"),
    )
    channel = models.CharField(max_length=100, choices=channel_choices)

    # Define Customer Type
    customer_type_choices = (
        (0, "مشتری"),
        (1, "مغازه دار"),
    )
    customer_type = models.CharField(max_length=100,
                                     choices=customer_type_choices)

    Customer_name = models.CharField(max_length=100)
    Customer_phone = models.CharField(max_length=100)

    # Production Date
    production_date_persian = jDateField()

    # Acceptance Status
    acceptance_status = models.BooleanField(default=True)
