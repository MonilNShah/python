# Generated by Django 2.0.2 on 2018-04-15 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20180414_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historydata',
            name='u_id',
            field=models.CharField(max_length=100),
        ),
    ]