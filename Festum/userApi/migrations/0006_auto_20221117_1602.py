# Generated by Django 3.2.7 on 2022-11-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApi', '0005_auto_20221117_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_place_ev',
            name='price_type',
            field=models.CharField(choices=[('per_day', 'PER DAY'), ('per_event', 'PER EVENT'), ('per_hour', 'PER HOUR')], default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='add_service_ev',
            name='service_price_type',
            field=models.CharField(choices=[('per_event', 'Per Event'), ('per_person', 'Per Person'), ('per_day', 'Per Day')], default='per_day', max_length=50),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='position',
            field=models.CharField(choices=[('2', 'EVENT VIEW PAGE'), ('1', 'EVENT LISTING PAGE'), ('0', 'HOME PAGE')], default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='createevent',
            name='discountId',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='createevent',
            name='serivceId',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='eventpersonaldetails',
            name='price_type',
            field=models.CharField(choices=[('per_day', 'PER DAY'), ('per_event', 'PER EVENT'), ('per_hour', 'PER HOUR')], default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='event_type',
            field=models.CharField(choices=[('group_skills', 'Group Skills Bussiness'), ('places', 'Have You Place'), ('personal_skills', 'Personal Skills Bussiness')], default='places', max_length=50),
        ),
        migrations.AlterField(
            model_name='pc_artist',
            name='price_type',
            field=models.CharField(choices=[('1', 'PER HOUR'), ('2', 'PER DAY')], default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='pc_equipments',
            name='equ_price_type',
            field=models.CharField(choices=[('1', 'PER HOUR'), ('2', 'PER DAY')], default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='place_events',
            name='IncludingFacilities',
            field=models.CharField(choices=[('romantic_candlelight_dinner', 'Romantic Candlelight Dinner'), ('romantic_stay', 'Romantic Stay'), ('romantic_lunch_dinner', 'Romantic Lunch/Dinner')], default='romantic_stay', max_length=100),
        ),
        migrations.AlterField(
            model_name='ps_equipments',
            name='equ_price_type',
            field=models.CharField(choices=[('1', 'PER HOUR'), ('2', 'PER DAY')], default=0, max_length=255),
        ),
    ]