# Generated by Django 4.2.5 on 2023-10-06 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_target_id_subdomain_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subdomains', to='home.target'),
        ),
    ]
