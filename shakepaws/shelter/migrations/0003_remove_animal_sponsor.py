# Generated by Django 3.1.3 on 2020-11-15 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0002_auto_20201115_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='sponsor',
        ),
    ]