# Generated by Django 5.0 on 2023-12-19 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_extraknowledge_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extraknowledge',
            options={'ordering': ['-date']},
        ),
    ]
