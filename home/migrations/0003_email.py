# Generated by Django 4.1 on 2022-08-12 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_products_product_medicine_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_email', models.EmailField(max_length=500)),
            ],
        ),
    ]
