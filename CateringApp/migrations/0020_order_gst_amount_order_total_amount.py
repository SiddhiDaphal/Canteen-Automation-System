# Generated by Django 4.2.2 on 2023-07-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CateringApp', '0019_userprofile_otp_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='gst_amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
