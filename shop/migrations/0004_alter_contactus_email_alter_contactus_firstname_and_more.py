# Generated by Django 4.0.4 on 2022-06-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='EMail',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='FirstName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='LastName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='TellMe',
            field=models.CharField(max_length=20000),
        ),
    ]