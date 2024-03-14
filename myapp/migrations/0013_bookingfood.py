# Generated by Django 3.2.5 on 2023-12-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_addemployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookingfood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('Itemname', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField()),
                ('Itemtype', models.CharField(max_length=100, null='true')),
                ('uploaded_image', models.FileField(upload_to='')),
                ('newquantity', models.IntegerField()),
                ('remarks', models.CharField(max_length=500)),
            ],
        ),
    ]