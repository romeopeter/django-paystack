# Generated by Django 3.0.4 on 2020-07-27 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Product',
            new_name='product',
        ),
    ]