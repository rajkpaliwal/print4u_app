# Generated by Django 3.1.1 on 2020-12-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
        ('photos', '0004_auto_20201025_1812'),
        ('cart', '0003_auto_20201107_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='documentid',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='documentid',
            field=models.ManyToManyField(blank=True, null=True, to='documents.Documents'),
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='photoid',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='photoid',
            field=models.ManyToManyField(blank=True, null=True, to='photos.Photos'),
        ),
    ]
