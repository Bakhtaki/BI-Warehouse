from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import post_save
from django_jalali.db.models import jDateField


# Create your models here
class Complaint(models.Model):
    Persian_year_choices = (
        ('1394', '1394'), ('1395', '1395'),
        ('1396', '1396'), ('1397', '1397'),
        ('1398', '1398'), ('1399', '1399'),
        ('1400', '1400'), ('1401', '1401'),
        ('1402', '1402'), ('1403', '1403'),
        ('1404', '1404'), ('1405', '1405'),
        ('1406', '1406'), ('1407', '1407'),
        ('1408', '1408'), ('1409', '1409'),
    )

    # Persian_months
    Persian_months_choices = (
        ('01', 'فروردین'), ('02', 'اردیبهشت'),
        ('03', 'خرداد'), ('04', 'تیر'),
        ('05', 'مرداد'), ('06', 'شهریور'),
        ('07', 'مهر'), ('08', 'آبان'),
        ('09', 'آذر'), ('10', 'دی'),
        ('11', 'بهمن'), ('12', 'اسفند'),
    )

    # Customer Types
    customer_type_choices = [
        ('Consumer', 'Consumer'), ('Store Owner', 'Store Owner'),
        ('Distribution Company', 'Distribution Company'), ('Other', 'Other')
        ('legal', 'legal')
    ]

    # Complaints Category
    complaint_category_choices = [
        ('Product Quality', 'Product Quality'), ('Packaging', 'Packaging'),
        ('Price', 'Price'), ('Distribution', 'Distribution'),
        ('External Material', 'External Material'), ('Weight', 'Weight'),
        ('Other', 'Other')
    ]

    # External Material
    external_material_choices = [
        ('Plastic', 'Plastic'), ('Glass', 'Glass'),
        ('Metal', 'Metal'), ('Paper', 'Paper'),
        ('Wood', 'Wood'), ('Hair', 'Hair'),
        ('Glue', 'Glue'), ('Sugar', 'Sugar'),
        ('Other', 'Other')
    ]

    # Product Category
    product_category_choices = [
        ('Jelly Gum', 'Jelly Gum'),
        ('Marshmallow', 'Marshmallow'),
        ('Coffee', 'Coffee'), ('Bakeries', 'Bakeries'),
        ('Chocolate', 'Chocolate'),
        ('Gum', 'Gum'),
        ('Jelly Powder', 'Jelly Powder'),
        ('Angel Kiss', 'Angel Kiss'),
        ('Other', 'Other')
    ]

    # Production site
    production_site_choices = [
        ('Hashtgerd', 'Hashtgerd'),
        ('Firuzkuh', 'Firuzkuh'),
    ]

    # Production Shift
    production_shift_choices = [
        ('Day', 'Day'),
        ('Night', 'Night'),
    ]

    # Actions
    actions_choices = [
        ('under Process', 'under Process'),
        (' process review', ' process review'),
        ('No action', 'no action'),
    ]

    # Complaint Status
    complaint_status_choices = [
        ('1', 'Open'),
        ('0', 'Closed'),
    ]


    # Fields
    id = models.AutoField(primary_key=True)
    creation_date = jDateField(auto_now_add=True, null=True, blank=True)

    # ------------------Customer Information------------------ ##
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    customer_family = models.CharField(max_length=100, null=True, blank=True)
    customer_phone = models.CharField(max_length=100, null=True, blank=True)
    customer_address = models.CharField(max_length=100, null=True, blank=True)

    # ------------------Complaints Information------------------ ##
    Persian__year = models.CharField(
        max_length=4, choices=Persian_year_choices, default='1402')
    Persian__month = models.CharField(
        max_length=2, choices=Persian_months_choices, default='01')
    Persian__day = models.CharField(max_length=2, default='01')
    customer_type = models.CharField(
        max_length=20, choices=customer_type_choices, default='Consumer')
    accepted = models.BooleanField(default=True, null=True, blank=True)
    complaint_category = models.CharField(
        max_length=20, choices=complaint_category_choices, default='Other',
        null=True, blank=True)
    external_material = models.CharField(
        max_length=20, choices=external_material_choices, default='Other',
        null=True, blank=True)
    complaint_description = models.TextField(null=True, blank=True)

    # ------------------Product Information------------------ ##
    product_category = models.CharField(
        max_length=20, choices=product_category_choices, default='Other',
        null=True, blank=True)
    product_code = models.CharField(max_length=100, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_weight = models.CharField(max_length=100, null=True, blank=True)
    product_price = models.CharField(max_length=100, null=True, blank=True)
    product_barcode = models.CharField(max_length=100, null=True, blank=True)

    # ------------------Production Information------------------ ##
    Persian_production_year = models.CharField(
        max_length=4, choices=Persian_year_choices, default='1402',
        null=True, blank=True)
    Persian_production_month = models.CharField(
        max_length=2, choices=Persian_months_choices, default='01',
        null=True, blank=True)
    Persian_production_day = models.CharField(
        max_length=2, default='01', null=True, blank=True)
    production_site = models.CharField(
        max_length=20, choices=production_site_choices, default='Hashtgerd',
        null=True, blank=True)
    production_shift = models.CharField(
        max_length=20, choices=production_shift_choices, default='Day',
        null=True, blank=True)
    # ------------------------Action --------------------------------- ##
    action = models.CharField(
        max_length=20, choices=actions_choices, default='under Process',
        null=True, blank=True)
    
