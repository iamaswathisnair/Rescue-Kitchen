# Generated by Django 3.2.5 on 2023-12-08 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_bookingfood_ngoname'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingfood',
            name='w_status',
            field=models.CharField(choices=[('waiting', 'waiting'), ('Request Accepted', 'Request Accepted'), ('Request Denied', 'Request Denied')], default=1, max_length=30),
            preserve_default=False,
        ),
    ]
