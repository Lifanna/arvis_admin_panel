# Generated by Django 3.2.23 on 2024-01-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apk',
            name='apk_file',
            field=models.FileField(upload_to=''),
        ),
    ]
