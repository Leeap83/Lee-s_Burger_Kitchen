# Generated by Django 3.2 on 2021-05-10 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_custom_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_burger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('custom_name', models.CharField(max_length=254)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_burger', to='products.category')),
                ('ingredients', models.ManyToManyField(blank=True, related_name='ingredient', to='products.Ingredients')),
            ],
        ),
    ]
