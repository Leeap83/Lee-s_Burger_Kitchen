# Generated by Django 3.2 on 2021-06-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20210609_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_burger',
            name='buns',
        ),
        migrations.AddField(
            model_name='custom_burger',
            name='bun',
            field=models.ManyToManyField(blank=True, related_name='bun', to='products.Ingredients'),
        ),
    ]