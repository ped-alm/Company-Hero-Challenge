# Generated by Django 3.1.1 on 2020-09-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('company', '0002_auto_20200906_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='telephone',
            field=models.CharField(blank=True, max_length=31, null=True),
        ),
    ]
