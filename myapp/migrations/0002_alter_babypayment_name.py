# Generated by Django 4.2.11 on 2024-05-08 16:35

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babypayment',
            name='name',
            field=models.CharField(max_length=200, validators=[myapp.models.validate_letters]),
        ),
    ]
