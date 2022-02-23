# Generated by Django 4.0.2 on 2022-02-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(verbose_name='Link to Profile Image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=20, verbose_name='Last Name'),
        ),
    ]