# Generated by Django 3.2.7 on 2022-10-14 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApi', '0010_auto_20221014_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_place_ev',
            name='price_type',
            field=models.CharField(choices=[('per_day', 'PER DAY'), ('per_hour', 'PER HOUR'), ('per_event', 'PER EVENT')], default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='position',
            field=models.CharField(choices=[('0', 'HOME PAGE'), ('1', 'EVENT LISTING PAGE'), ('2', 'EVENT VIEW PAGE')], default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='createevent',
            name='event_type',
            field=models.CharField(choices=[('places', 'Have You Place'), ('group_skills', 'Group Skills Bussiness'), ('personal_skills', 'Personal Skills Bussiness')], default='places', max_length=50),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='discount_type',
            field=models.CharField(choices=[('advance_and_discount_confirmation', 'Advance And Discount Confirmation'), ('discount_on_equipment_or_item', 'Discount On Equipment Or Item'), ('discount_on_total_bill', 'Discount On Total Bill')], max_length=50),
        ),
        migrations.AlterField(
            model_name='eventpersonaldetails',
            name='price_type',
            field=models.CharField(choices=[('per_day', 'PER DAY'), ('per_hour', 'PER HOUR'), ('per_event', 'PER EVENT')], default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='event_type',
            field=models.CharField(choices=[('places', 'Have You Place'), ('group_skills', 'Group Skills Bussiness'), ('personal_skills', 'Personal Skills Bussiness')], default='places', max_length=50),
        ),
        migrations.AlterField(
            model_name='place_events',
            name='IncludingFacilities',
            field=models.CharField(choices=[('romantic_stay', 'Romantic Stay'), ('romantic_lunch_dinner', 'Romantic Lunch/Dinner'), ('romantic_candlelight_dinner', 'Romantic Candlelight Dinner')], default='romantic_stay', max_length=100),
        ),
        migrations.CreateModel(
            name='PlaceEventType',
            fields=[
                ('placeId', models.AutoField(primary_key=True, serialize=False)),
                ('place_banner', models.ImageField(blank=True, null=True, upload_to='place/banner/')),
                ('place_price', models.FloatField(max_length=50)),
                ('price_type', models.CharField(choices=[('per_day', 'PER DAY'), ('per_hour', 'PER HOUR'), ('per_event', 'PER EVENT')], default=0, max_length=255)),
                ('details', models.CharField(blank=True, max_length=2500)),
                ('is_active', models.BooleanField(default=True)),
                ('timestampe', models.DateTimeField(auto_now_add=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_id', to='userApi.eventtype')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
