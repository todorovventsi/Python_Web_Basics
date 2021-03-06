# Generated by Django 4.0.2 on 2022-02-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_profile_age_alter_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='note',
            name='image',
            field=models.URLField(verbose_name='Link To Image'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Title'),
        ),
    ]
