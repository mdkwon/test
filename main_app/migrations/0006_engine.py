# Generated by Django 2.2.1 on 2019-06-06 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20190519_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_size', models.CharField(max_length=255)),
                ('make_name', models.ManyToManyField(to='main_app.Make')),
                ('model_name', models.ManyToManyField(to='main_app.CarModel')),
                ('model_year', models.ManyToManyField(to='main_app.Year')),
            ],
        ),
    ]
