# Generated by Django 3.1.1 on 2020-10-31 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201025_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='staus',
            field=models.IntegerField(null=True),
        ),
    ]
