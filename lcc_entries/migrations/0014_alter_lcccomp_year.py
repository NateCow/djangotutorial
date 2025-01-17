# Generated by Django 5.1.5 on 2025-01-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcc_entries', '0013_alter_lcccomp_name_alter_lcccomp_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lcccomp',
            name='year',
            field=models.IntegerField(choices=[(2002, 2002), (2004, 2004), (2005, 2005), (2005, 2005), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], unique=True),
        ),
    ]
