# Generated by Django 4.0 on 2021-12-19 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0006_alter_company_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='comapny_category',
            field=models.CharField(blank=True, choices=[('Internet Shop', 'Internet Shop'), ('SuperMarket', 'SuperMarket'), ('Shopping center', 'Shopping center'), ('Furniture Shop', 'Furniture Shop'), ('IT Company', 'IT Company'), ('Educational Center', 'Educational Center')], max_length=40),
        ),
    ]
