# Generated by Django 4.2.11 on 2024-04-30 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_uniquesitternumberfield_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UniqueSitterNumberField',
        ),
        migrations.AddField(
            model_name='babysitter',
            name='Sitter_Number',
            field=models.CharField(default=True, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
