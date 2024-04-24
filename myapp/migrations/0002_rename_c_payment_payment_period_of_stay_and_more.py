# Generated by Django 4.2.11 on 2024-04-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='c_payment',
            new_name='period_of_stay',
        ),
        migrations.AddField(
            model_name='payment',
            name='paid_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
