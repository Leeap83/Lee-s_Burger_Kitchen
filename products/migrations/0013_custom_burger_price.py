# Generated by Django 3.2 on 2021-06-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_burger',
            name='price',
            field=models.DecimalField(decimal_places=2, default='10.99', editable=False, max_digits=6),
        ),
    ]
