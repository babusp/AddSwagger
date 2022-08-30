# Generated by Django 4.0.6 on 2022-08-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ViewSets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.CharField(max_length=230),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.CharField(max_length=230),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.CharField(max_length=230),
        ),
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.CharField(max_length=230),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=230, unique=True),
        ),
    ]
