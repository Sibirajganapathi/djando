from django.db import models

class EnquiryForm(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=12)
    mobile=models.CharField(max_length=200)
