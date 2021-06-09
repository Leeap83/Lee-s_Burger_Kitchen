# Generated by Django 3.2 on 2021-06-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20210609_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_burger',
            name='buns',
        ),
        migrations.RemoveField(
            model_name='custom_burger',
            name='burger',
        ),
        migrations.RemoveField(
            model_name='custom_burger',
            name='category',
        ),
        migrations.RemoveField(
            model_name='custom_burger',
            name='cheese',
        ),
        migrations.RemoveField(
            model_name='custom_burger',
            name='extras',
        ),
        migrations.RemoveField(
            model_name='custom_burger',
            name='salads',
        ),
        migrations.RemoveField(
            model_name='custom_burger',
            name='sauce',
        ),
        migrations.AddField(
            model_name='custom_burger',
            name='ingredients',
            field=models.ManyToManyField(blank=True, related_name='ingredient', to='products.Ingredients'),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='cyo',
            field=models.BooleanField(default=False),
        ),
    ]
