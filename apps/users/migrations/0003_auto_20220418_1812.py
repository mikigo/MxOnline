# Generated by Django 2.2 on 2022-04-18 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220418_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='手机号码'),
        ),
    ]
