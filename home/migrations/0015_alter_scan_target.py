# Generated by Django 4.2.5 on 2023-10-06 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_subdomain_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.target'),
        ),
    ]
