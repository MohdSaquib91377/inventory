# Generated by Django 3.1.3 on 2020-11-27 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20201127_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
    ]
