# Generated by Django 4.0.4 on 2022-07-18 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_order_customer_id_order_cart_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(related_name='categories', through='app.CategoryProduct', to='app.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.cart'),
            preserve_default=False,
        ),
    ]
