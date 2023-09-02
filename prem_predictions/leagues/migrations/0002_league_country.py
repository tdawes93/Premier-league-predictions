# Generated by Django 4.2.4 on 2023-09-02 14:13

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
