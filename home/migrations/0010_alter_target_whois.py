# Generated by Django 4.2.5 on 2023-10-05 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_whois_target_target_whois'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='whois',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.whois'),
        ),
    ]
