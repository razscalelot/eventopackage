# Generated by Django 3.2.7 on 2022-10-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApi', '0009_auto_20221014_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventtype',
            old_name='category',
            new_name='category_id',
        ),
        migrations.AlterField(
            model_name='add_place_ev',
            name='price_type',
            field=models.CharField(choices=[('per_event', 'PER EVENT'), ('per_hour', 'PER HOUR'), ('per_day', 'PER DAY')], default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='position',
            field=models.CharField(choices=[('2', 'EVENT VIEW PAGE'), ('0', 'HOME PAGE'), ('1', 'EVENT LISTING PAGE')], default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='createevent',
            name='event_type',
            field=models.CharField(choices=[('personal_skills', 'Personal Skills Bussiness'), ('places', 'Have You Place'), ('group_skills', 'Group Skills Bussiness')], default='places', max_length=50),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='discount_type',
            field=models.CharField(choices=[('discount_on_equipment_or_item', 'Discount On Equipment Or Item'), ('discount_on_total_bill', 'Discount On Total Bill'), ('advance_and_discount_confirmation', 'Advance And Discount Confirmation')], max_length=50),
        ),
        migrations.AlterField(
            model_name='eventpersonaldetails',
            name='price_type',
            field=models.CharField(choices=[('per_event', 'PER EVENT'), ('per_hour', 'PER HOUR'), ('per_day', 'PER DAY')], default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='event_type',
            field=models.CharField(choices=[('personal_skills', 'Personal Skills Bussiness'), ('places', 'Have You Place'), ('group_skills', 'Group Skills Bussiness')], default='places', max_length=50),
        ),
    ]
