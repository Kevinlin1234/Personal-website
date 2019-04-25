# Generated by Django 2.0.7 on 2019-04-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_person_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='firstname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastname',
            field=models.CharField(max_length=20),
        ),
    ]
