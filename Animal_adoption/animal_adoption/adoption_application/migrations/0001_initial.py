# Generated by Django 4.2.6 on 2023-10-10 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptionApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('manager_comments', models.TextField(blank=True)),
                ('adopter_inquiries', models.TextField(blank=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('residence_or_outdoor_space', models.TextField(blank=True)),
                ('number_of_existing_pets', models.PositiveIntegerField(blank=True, default=0)),
                ('pet_care_routine', models.TextField(blank=True)),
                ('training_and_Socialization', models.TextField(blank=True)),
            ],
        ),
    ]
