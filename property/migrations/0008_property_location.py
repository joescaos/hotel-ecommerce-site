# Generated by Django 3.0.5 on 2020-06-02 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]