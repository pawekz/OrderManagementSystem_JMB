# Generated by Django 5.0.6 on 2024-05-09 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10),
        ),
    ]
