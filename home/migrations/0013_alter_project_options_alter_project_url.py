# Generated by Django 4.2.7 on 2023-12-01 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_projectimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
