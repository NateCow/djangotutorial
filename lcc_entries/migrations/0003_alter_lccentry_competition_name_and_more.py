# Generated by Django 5.1.5 on 2025-01-17 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcc_entries', '0002_lcccomp_alter_lcccreator_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lccentry',
            name='competition_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='lccentry',
            name='competition_year',
            field=models.IntegerField(),
        ),
    ]
