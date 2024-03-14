# Generated by Django 3.2.5 on 2023-12-08 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_bookingfood_workername'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addfood',
            name='status',
        ),
        migrations.AddField(
            model_name='bookingfood',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('done', 'done'), ('over', 'over')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]