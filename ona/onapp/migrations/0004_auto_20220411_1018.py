# Generated by Django 3.0.1 on 2022-04-11 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onapp', '0003_auto_20220411_0932'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EndDate',
        ),
        migrations.AddField(
            model_name='startdate',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
