# Generated by Django 4.1.1 on 2022-09-22 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_alter_cartitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='price',
        ),
    ]
