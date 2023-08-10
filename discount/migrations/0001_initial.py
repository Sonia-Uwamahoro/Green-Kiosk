# Generated by Django 4.2.3 on 2023-07-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=32)),
                ('code', models.IntegerField(default=0)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=6)),
                ('expiry_date', models.DateField(auto_now=True)),
                ('minimum_purchase', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]