# Generated by Django 5.1.5 on 2025-01-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcc_entries', '0036_remove_lcccomp_end_date_lcccomp_deadline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lcccomp',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
