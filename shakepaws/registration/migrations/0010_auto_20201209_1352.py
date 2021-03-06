# Generated by Django 3.1.2 on 2020-12-09 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_profile_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile_animal',
            options={'ordering': ['-created'], 'verbose_name': 'Apadrinamiento de usuario', 'verbose_name_plural': 'Apadrinamientos de usuarios'},
        ),
        migrations.AddField(
            model_name='profile_animal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
    ]
