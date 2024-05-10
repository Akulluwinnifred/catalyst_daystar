# Generated by Django 4.2.11 on 2024-05-09 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_babypayment_full_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babypayment',
            name='full_day',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='babypayment',
            name='half_day',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='babypayment',
            name='monthly',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='babypayment',
            name='remaining_balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='babypayment',
            name='total_amount_due',
            field=models.DecimalField(blank=True, decimal_places=2, default=False, max_digits=10),
        ),
    ]