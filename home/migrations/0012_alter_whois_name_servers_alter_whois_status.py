# Generated by Django 4.2.5 on 2023-10-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_whois_domain_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whois',
            name='name_servers',
            field=models.JSONField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='whois',
            name='status',
            field=models.JSONField(blank=True, max_length=20000, null=True),
        ),
    ]
