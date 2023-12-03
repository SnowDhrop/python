# Generated by Django 4.2.7 on 2023-12-03 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='date',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='is_ordered',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
