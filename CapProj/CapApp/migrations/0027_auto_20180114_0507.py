# Generated by Django 2.0.1 on 2018-01-14 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CapApp', '0026_auto_20180112_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='core_project_num',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='grant',
            name='pi_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
