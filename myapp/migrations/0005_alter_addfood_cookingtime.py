# Generated by Django 3.2.5 on 2023-11-26 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_addfood_datee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addfood',
            name='cookingtime',
            field=models.TimeField(null=True),
        ),
    ]