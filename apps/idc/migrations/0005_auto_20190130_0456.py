# Generated by Django 2.1 on 2019-01-29 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idc', '0004_auto_20190130_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinet',
            name='idc',
            field=models.ForeignKey(help_text='所属机房', null=True, on_delete=django.db.models.deletion.CASCADE, to='idc.Idc', verbose_name='所处机房'),
        ),
    ]