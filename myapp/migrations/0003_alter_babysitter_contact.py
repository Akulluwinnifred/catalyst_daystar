# Generated by Django 4.2.11 on 2024-05-02 06:45

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_babysitter_nin_alter_babysitter_next_of_kin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babysitter',
            name='Contact',
            field=models.CharField(max_length=10, validators=[myapp.models.validate_contact_length]),
        ),
    ]
