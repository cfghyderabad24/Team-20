from django.db import models


# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username


class FarmerFields(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    SEASON_CHOICES = [
        ('Summer', 'Summer'),
        ('Winter', 'Winter'),
        ('Monsoon', 'Monsoon'),
    ]

    SEEDS_USED_CHOICES = [
        ('Own', 'Own'),
        ('Given by IFTR', 'Given by IFTR'),
    ]

    TRANSPLANTING_CHOICES = [
        ('Manual', 'Manual'),
        ('Machine', 'Machine'),
    ]

    IRRIGATION_METHOD_CHOICES = [
        ('Borewell', 'Borewell'),
        ('Well', 'Well'),
        ('River', 'River'),
        ('Drip Irrigation', 'Drip Irrigation'),
    ]

    FERTILISERS_USED_CHOICES = [
        ('Organic', 'Organic'),
        ('Chemical', 'Chemical'),
        ('Bio-inputs', 'Bio-inputs'),
    ]

    FINANCIAL_NEED_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    aadhar_number = models.CharField(max_length=12)
    contact_number = models.CharField(max_length=10)
    area_ploughed = models.DecimalField(max_digits=5, decimal_places=2)
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)
    crops_grown = models.TextField()
    seeds_used = models.CharField(max_length=15, choices=SEEDS_USED_CHOICES)
    date_of_seed_sown = models.DateField()
    transplanting = models.CharField(max_length=10, choices=TRANSPLANTING_CHOICES)
    irrigation_method = models.CharField(max_length=20, choices=IRRIGATION_METHOD_CHOICES)
    fertilisers_used = models.CharField(max_length=10, choices=FERTILISERS_USED_CHOICES)
    date_of_harvesting = models.DateField()
    yield_in_kg = models.DecimalField(max_digits=10, decimal_places=2)
    financial_need = models.CharField(max_length=3, choices=FINANCIAL_NEED_CHOICES)

    class Meta:
        db_table="form_table"

    def __str__(self):
        return self.name


class Farmer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "farmer_table"

    def __str__(self):
        return self.username
