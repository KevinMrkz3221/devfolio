# Generated by Django 4.2.7 on 2023-11-27 23:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_experience_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['-start_date']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['-level']},
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/projects'),
        ),
    ]