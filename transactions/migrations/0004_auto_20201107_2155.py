# Generated by Django 3.1.1 on 2020-11-07 21:55

from django.db import migrations, models
from datetime import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20201025_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='transactiondate',
            field=models.DateTimeField(auto_now_add=True, default= datetime.now()),
            preserve_default=False,
        ),
    ]
