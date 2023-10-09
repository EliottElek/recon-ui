# Generated by Django 4.2.5 on 2023-10-07 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_remove_target_ip_target_domain_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipinfos',
            name='last_updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='ipinfos',
            name='location_continent',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ipinfos',
            name='location_country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ipinfos',
            name='location_country_code',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ipinfos',
            name='location_latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ipinfos',
            name='location_longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ipinfos',
            name='location_registered_country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ipinfos',
            name='location_registered_country_code',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ipinfos',
            name='location_timezone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ipinfos',
            name='location_updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]