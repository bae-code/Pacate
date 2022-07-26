# Generated by Django 4.0.6 on 2022-07-26 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_customusermodel_main_species'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caresheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('sex', models.CharField(max_length=20, verbose_name='성별')),
                ('morph', models.CharField(max_length=20, verbose_name='모프')),
                ('weight', models.FloatField(verbose_name='무게')),
                ('regist_date', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Master', to='user.customusermodel')),
            ],
        ),
    ]
