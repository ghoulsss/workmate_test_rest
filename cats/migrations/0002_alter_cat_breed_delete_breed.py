# Generated by Django 5.1.1 on 2024-09-30 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='breed',
            field=models.CharField(max_length=55),
        ),
        migrations.DeleteModel(
            name='Breed',
        ),
    ]
