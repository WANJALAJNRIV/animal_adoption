# Generated by Django 4.1.7 on 2023-10-10 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_pet_fee_pet_gender_pet_state_pet_suburb_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='fee',
        ),
    ]