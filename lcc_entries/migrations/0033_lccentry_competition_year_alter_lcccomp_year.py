# Generated by Django 5.1.5 on 2025-01-22 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcc_entries', '0032_lccentry_content_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='lccentry',
            name='competition_year',
            field=models.ForeignKey(default='2002', on_delete=django.db.models.deletion.CASCADE, related_name='entries_by_year', to='lcc_entries.lcccomp', to_field='year'),
        ),
        migrations.AlterField(
            model_name='lcccomp',
            name='year',
            field=models.CharField(choices=[('LCC01', 2002), ('LCC02', 2004), ('LCC03', 2004), ('LCC04', 2005), ('LCC05', 2007), ('LCC06', 2008), ('LCC07', 2009), ('LCC08', 2010), ('LCC09', 2011), ('LCC10', 2012), ('LCC11', 2013), ('LCC12', 2014), ('LCC2015', 2015), ('LCC2016', 2016), ('LCC2017', 2017), ('LCC2018', 2018), ('SC19', 2019), ('SC20', 2020), ('SC21', 2021), ('SC22', 2022), ('SC23', 2023), ('SC24', 2024)], max_length=200, unique=True),
        ),
    ]
