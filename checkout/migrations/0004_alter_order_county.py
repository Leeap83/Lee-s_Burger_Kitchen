# Generated by Django 3.2 on 2021-06-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_remove_order_order_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
