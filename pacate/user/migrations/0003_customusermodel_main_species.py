# Generated by Django 4.0.6 on 2022-07-26 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_user_customusermodel_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='main_species',
            field=models.CharField(max_length=20, null=True, verbose_name='사육종'),
        ),
    ]
