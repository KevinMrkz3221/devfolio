# Generated by Django 5.0 on 2023-12-19 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_extraknowledge_alter_experience_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='extraknowledge',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]