# Generated by Django 4.0 on 2021-12-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0004_alter_company_comapny_category_alter_rate_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='comapny_category',
            field=models.CharField(choices=[('Internet Shop', 'Internet Shop'), ('SuperMarket', 'SuperMarket'), ('Shopping center', 'Shopping center'), ('Furniture Shop', 'Furniture Shop'), ('IT Company', 'IT Company'), ('Educational Center', 'Educational Center'), ('DEFAULT', 'DEFAULT')], default='DF', max_length=40),
        ),
    ]
