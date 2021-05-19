# Generated by Django 3.2 on 2021-05-18 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, '1/5'), (2, '2/5 '), (3, '3/5'), (4, '4/5'), (5, '5/5')]),
        ),
    ]
