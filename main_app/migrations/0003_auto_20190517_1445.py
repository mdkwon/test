# Generated by Django 2.2.1 on 2019-05-17 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20190517_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='make_name',
            field=models.ManyToManyField(to='main_app.Make'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='model_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.Year'),
        ),
    ]