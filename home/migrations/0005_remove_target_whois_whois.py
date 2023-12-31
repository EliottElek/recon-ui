# Generated by Django 4.2.5 on 2023-10-05 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_subdomain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target',
            name='whois',
        ),
        migrations.CreateModel(
            name='Whois',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=100)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('expires', models.DateTimeField()),
                ('registrar', models.CharField(max_length=100)),
                ('registrar_abuse_email', models.EmailField(max_length=254)),
                ('registrar_abuse_phone', models.CharField(max_length=20)),
                ('registrant_name', models.CharField(blank=True, max_length=100, null=True)),
                ('registrant_organization', models.CharField(blank=True, max_length=100, null=True)),
                ('registrant_address', models.CharField(blank=True, max_length=100, null=True)),
                ('registrant_city', models.CharField(blank=True, max_length=50, null=True)),
                ('registrant_state', models.CharField(blank=True, max_length=50, null=True)),
                ('registrant_zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('registrant_country', models.CharField(blank=True, max_length=50, null=True)),
                ('registrant_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('dnssec', models.CharField(max_length=20)),
                ('status', models.JSONField()),
                ('name_servers', models.JSONField()),
                ('admin_name', models.CharField(blank=True, max_length=100, null=True)),
                ('admin_id', models.CharField(blank=True, max_length=100, null=True)),
                ('admin_organization', models.CharField(blank=True, max_length=100, null=True)),
                ('admin_city', models.CharField(blank=True, max_length=50, null=True)),
                ('admin_address', models.CharField(blank=True, max_length=100, null=True)),
                ('admin_state', models.CharField(blank=True, max_length=50, null=True)),
                ('admin_zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('admin_country', models.CharField(blank=True, max_length=50, null=True)),
                ('admin_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('admin_fax', models.CharField(blank=True, max_length=20, null=True)),
                ('admin_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('billing_name', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_id', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_organization', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=50, null=True)),
                ('billing_address', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_state', models.CharField(blank=True, max_length=50, null=True)),
                ('billing_zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_country', models.CharField(blank=True, max_length=50, null=True)),
                ('billing_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_fax', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('tech_name', models.CharField(blank=True, max_length=100, null=True)),
                ('tech_id', models.CharField(blank=True, max_length=100, null=True)),
                ('tech_organization', models.CharField(blank=True, max_length=100, null=True)),
                ('tech_city', models.CharField(blank=True, max_length=50, null=True)),
                ('tech_address', models.CharField(blank=True, max_length=100, null=True)),
                ('tech_state', models.CharField(blank=True, max_length=50, null=True)),
                ('tech_zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('tech_country', models.CharField(blank=True, max_length=50, null=True)),
                ('tech_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('tech_fax', models.CharField(blank=True, max_length=20, null=True)),
                ('tech_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.target')),
            ],
        ),
    ]
