# Generated by Django 5.0.4 on 2024-04-24 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
