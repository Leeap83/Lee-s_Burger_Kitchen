# Generated by Django 3.2 on 2021-06-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20210609_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_burger',
            name='bun',
        ),
        migrations.RemoveField(
            model_name='custom_burger',
            name='burgers',
        ),
        migrations.RemoveField(
            model_name='custom_burger',
            name='cheeses',
        ),
        migrations.RemoveField(
            model_name='custom_burger',
            name='extra',
        ),
        migrations.RemoveField(
            model_name='custom_burger',
            name='salad',
        ),
        migrations.RemoveField(
            model_name='custom_burger',
            name='sauces',
        ),
        migrations.AddField(
            model_name='custom_burger',
            name='buns',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='custom_burger',
            name='burger',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='custom_burger',
            name='cheese',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='custom_burger',
            name='extras',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='custom_burger',
            name='salads',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='custom_burger',
            name='sauce',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
