# Generated by Django 4.2.5 on 2023-10-05 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_whois_scan_certfinder_scan_nuclei_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='whois',
            field=models.CharField(default='', max_length=1000000),
        ),
    ]