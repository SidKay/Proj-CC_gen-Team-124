# Generated by Django 4.1 on 2022-08-13 20:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_designinfo_design_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='designinfo',
            name='design_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]