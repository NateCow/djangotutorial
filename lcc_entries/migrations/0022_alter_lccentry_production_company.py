# Generated by Django 5.1.5 on 2025-01-17 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcc_entries', '0021_lccentry_status_lccentry_top_10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lccentry',
            name='production_company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
