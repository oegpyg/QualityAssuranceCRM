from django.db import models

class UserProfile(models.Model):
    new_field = models.CharField(max_length=140, default='SOME STRING')
    image_field = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)

class CompanyData(models.Model):
    site_name = models.CharField(max_length=255)
    admin_email = models.EmailField()