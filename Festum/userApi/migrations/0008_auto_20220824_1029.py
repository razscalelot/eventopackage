# Generated by Django 3.2.7 on 2022-08-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApi', '0007_auto_20220824_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_service_ev',
            name='service_price_type',
            field=models.CharField(choices=[('per_person', 'Per Person'), ('per_day', 'Per Day'), ('per_event', 'Per Event')], default='per_day', max_length=50),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='position',
            field=models.CharField(choices=[('2', 'EVENT VIEW PAGE'), ('0', 'HOME PAGE'), ('1', 'EVENT LISTING PAGE')], default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='discount_type',
            field=models.CharField(choices=[('discount_on_equipment_or_item', 'Discount On Equipment Or Item'), ('advance_and_discount_confirmation', 'Advance And Discount Confirmation'), ('discount_on_total_bill', 'Discount On Total Bill')], max_length=50),
        ),
        migrations.AlterField(
            model_name='place_events',
            name='IncludingFacilities',
            field=models.CharField(choices=[('romantic_candlelight_dinner', 'Romantic Candlelight Dinner'), ('romantic_lunch_dinner', 'Romantic Lunch/Dinner'), ('romantic_stay', 'Romantic Stay')], default='romantic_stay', max_length=100),
        ),
    ]
