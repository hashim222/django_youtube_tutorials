# Generated by Django 4.1 on 2022-08-11 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]