# Generated by Django 5.1.5 on 2025-02-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebda3', '0011_offer_offer_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='phone_number',
            field=models.CharField(default='01067343755', max_length=200),
        ),
    ]
