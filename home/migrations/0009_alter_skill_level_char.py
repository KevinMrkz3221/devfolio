# Generated by Django 4.2.7 on 2023-11-28 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_skill_level_char'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level_char',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]