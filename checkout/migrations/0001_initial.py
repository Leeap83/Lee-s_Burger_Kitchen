# Generated by Django 3.2 on 2021-05-21 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0008_custom_burger'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.CharField(editable=False, max_length=32)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('phone_number', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=80)),
                ('town_or_city', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=20)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_status', models.CharField(choices=[('Order Recieved', 'Order Recieved'), ('Cooking', 'Cooking'), ('Out for delivery', 'Out for Delivery'), ('Order Delivered', 'Order Delivered')], default='Order Recieved', max_length=100)),
                ('original_cart', models.TextField(default='')),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
