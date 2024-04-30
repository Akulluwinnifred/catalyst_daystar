# Generated by Django 4.2.11 on 2024-04-30 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueSitterNumberField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='Sitter_Number',
        ),
        migrations.AlterField(
            model_name='babysitterattendance',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.babysitter'),
        ),
    ]
