# Generated by Django 5.1.5 on 2025-01-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcc_entries', '0038_remove_lcccomp_is_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='lccentry',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
