# Generated by Django 3.2.7 on 2022-09-05 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApi', '0010_auto_20220905_1441'),
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
            field=models.CharField(choices=[('per_day', 'Per Day'), ('per_person', 'Per Person'), ('per_event', 'Per Event')], default='per_day', max_length=50),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='position',
            field=models.CharField(choices=[('2', 'EVENT VIEW PAGE'), ('1', 'EVENT LISTING PAGE'), ('0', 'HOME PAGE')], default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='createevent',
            name='event_type',
            field=models.CharField(choices=[('group_skills', 'Group Skills Bussiness'), ('places', 'Have You Place'), ('personal_skills', 'Personal Skills Bussiness')], default='places', max_length=50),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='discount_type',
            field=models.CharField(choices=[('discount_on_equipment_or_item', 'Discount On Equipment Or Item'), ('advance_and_discount_confirmation', 'Advance And Discount Confirmation'), ('discount_on_total_bill', 'Discount On Total Bill')], max_length=50),
        ),
        migrations.AlterField(
            model_name='eventcategory',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='userApi.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place_events',
            name='IncludingFacilities',
            field=models.CharField(choices=[('romantic_lunch_dinner', 'Romantic Lunch/Dinner'), ('romantic_stay', 'Romantic Stay'), ('romantic_candlelight_dinner', 'Romantic Candlelight Dinner')], default='romantic_stay', max_length=100),
        ),
    ]
