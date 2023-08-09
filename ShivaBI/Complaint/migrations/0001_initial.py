# Generated by Django 4.2.4 on 2023-08-09 05:51

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Complaint",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("complaint_date_persian", django_jalali.db.models.jDateField()),
                ("complaint_date", models.DateField()),
                (
                    "channel",
                    models.CharField(
                        choices=[
                            (0, "Phone"),
                            (1, "Social Media"),
                            (2, "Distribution Company"),
                            (3, "Website"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "customer_type",
                    models.CharField(
                        choices=[(0, "مشتری"), (1, "مغازه دار")], max_length=100
                    ),
                ),
                ("Customer_name", models.CharField(max_length=100)),
                ("Customer_phone", models.CharField(max_length=100)),
                ("production_date_persian", django_jalali.db.models.jDateField()),
                ("acceptance_status", models.BooleanField(default=True)),
                ("complaint_title", models.CharField(max_length=100)),
                ("packaging_complaint", models.BooleanField(default=False)),
                ("product_colors_complaint", models.BooleanField(default=False)),
                ("product_shapes_complaint", models.BooleanField(default=False)),
                (
                    "thing",
                    models.CharField(
                        choices=[
                            (0, "wood"),
                            (1, "metal"),
                            (2, "plastic"),
                            (3, "Hair"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "product_category",
                    models.CharField(
                        choices=[
                            (0, "Jelly Gum"),
                            (1, "Jelly Powder"),
                            (2, "Extruderies"),
                            (3, "Coffee"),
                            (4, "Bakery"),
                            (5, "Marshmallow"),
                        ],
                        max_length=100,
                    ),
                ),
                ("product_name", models.CharField(max_length=100)),
                ("product_code", models.CharField(max_length=100)),
                ("product_batch", models.CharField(max_length=13)),
                ("complaint_quantity", models.IntegerField()),
                (
                    "production_shift",
                    models.CharField(
                        choices=[(0, "Day"), (1, "Night")], max_length=100
                    ),
                ),
                (
                    "production_site",
                    models.CharField(
                        choices=[(0, "Hashtgerd"), (1, "FiruzKuh")], max_length=100
                    ),
                ),
                ("send_gift", models.BooleanField(default=False)),
                (
                    "gift_type",
                    models.CharField(
                        choices=[(0, "Money"), (1, "Product")], max_length=100
                    ),
                ),
                (
                    "complaint_result",
                    models.CharField(
                        choices=[
                            (0, "Process Review"),
                            (1, "Investigation"),
                            (2, "None"),
                        ],
                        max_length=100,
                    ),
                ),
                ("complaint_description", models.TextField(max_length=1000)),
            ],
        ),
    ]
