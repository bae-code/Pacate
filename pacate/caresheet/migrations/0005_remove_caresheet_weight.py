# Generated by Django 4.0.6 on 2022-07-26 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caresheet', '0004_alter_weightrecord_record_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caresheet',
            name='weight',
        ),
    ]
