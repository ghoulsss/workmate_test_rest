# Generated by Django 5.1.1 on 2024-09-30 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_alter_cat_breed_delete_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='owner',
            field=models.CharField(max_length=55),
        ),
    ]
