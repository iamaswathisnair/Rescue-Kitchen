# Generated by Django 3.2.5 on 2023-11-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_addfood_cookingtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addfood',
            name='datee',
            field=models.DateField(null=True),
        ),
    ]
