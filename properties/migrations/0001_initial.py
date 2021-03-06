# Generated by Django 3.0.5 on 2020-04-21 18:20

from django.db import migrations, models
import django.utils.timezone
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('location', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('bedrooms', models.CharField(max_length=255)),
                ('agent', models.CharField(max_length=255)),
                ('agent_contact', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('agent_email', models.EmailField(max_length=255)),
                ('agent_company', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
