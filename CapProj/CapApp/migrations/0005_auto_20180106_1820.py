# Generated by Django 2.0.1 on 2018-01-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CapApp', '0004_auto_20180106_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='pi_ids',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='grant',
            name='project_terms',
            field=models.TextField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='grant',
            name='project_title',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
