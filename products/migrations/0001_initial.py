# Generated by Django 4.1.1 on 2022-09-22 04:48

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.models.file_path)),
                ('title', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
            ],
        ),
    ]
