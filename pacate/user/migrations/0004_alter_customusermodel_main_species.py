# Generated by Django 4.0.6 on 2022-07-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customusermodel_main_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='main_species',
            field=models.CharField(choices=[('crested', '크레스티드게코'), ('x', '준비중')], default=1, max_length=20, verbose_name='사육종'),
            preserve_default=False,
        ),
    ]
