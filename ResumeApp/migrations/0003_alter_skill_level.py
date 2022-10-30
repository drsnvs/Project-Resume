# Generated by Django 4.1.2 on 2022-10-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResumeApp', '0002_skill_known'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='Level',
            field=models.CharField(choices=[(1, 'beginner'), (2, 'intermediate'), (3, 'advance')], max_length=10),
        ),
    ]