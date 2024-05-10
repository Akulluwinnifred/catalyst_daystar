# Generated by Django 4.2.11 on 2024-05-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_babypayment_full_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babypayment',
            name='total_amount_due',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]