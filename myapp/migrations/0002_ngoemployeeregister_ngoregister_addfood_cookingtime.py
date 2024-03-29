# Generated by Django 4.2.5 on 2023-10-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NGOemployeeregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30)),
                ('Lastname', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=30)),
                ('Contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NGOregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30)),
                ('Lastname', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=30)),
                ('Contact', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='addfood',
            name='cookingtime',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
