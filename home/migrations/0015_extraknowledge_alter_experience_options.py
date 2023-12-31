# Generated by Django 5.0 on 2023-12-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_experience_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraKnowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/extra_knowledge')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='static/extra_knowledge')),
            ],
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['-start_date']},
        ),
    ]
