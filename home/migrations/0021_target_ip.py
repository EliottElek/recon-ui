# Generated by Django 4.2.5 on 2023-10-07 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_ipinfos_alter_target_ip_infos'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='ip',
            field=models.CharField(default='', max_length=100),
        ),
    ]
