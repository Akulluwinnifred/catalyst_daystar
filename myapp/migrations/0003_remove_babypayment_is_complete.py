# Generated by Django 4.2.11 on 2024-05-20 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_babypayment_is_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='babypayment',
            name='is_complete',
        ),
    ]