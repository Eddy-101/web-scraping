from django.db import models
import os
import datetime

# Create your models here.
def file_path(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Product(models.Model):
    image = models.ImageField(upload_to=file_path, null=True, blank=True)
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
