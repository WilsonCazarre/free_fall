# Generated by Django 3.1.2 on 2020-10-19 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201019_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemap',
            name='portrait',
            field=models.ImageField(null=True, upload_to='map_portraits'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='portrait',
            field=models.ImageField(null=True, upload_to='hero_portraits'),
        ),
    ]
