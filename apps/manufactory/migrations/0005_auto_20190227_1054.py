# Generated by Django 2.1 on 2019-02-27 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manufactory', '0004_auto_20190216_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufactory',
            old_name='tel_num',
            new_name='phone',
        ),
    ]
