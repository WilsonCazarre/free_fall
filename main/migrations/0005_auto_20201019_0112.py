# Generated by Django 3.1.2 on 2020-10-19 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201019_0106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gamemap',
            options={'ordering': ('name',)},
        ),
    ]
