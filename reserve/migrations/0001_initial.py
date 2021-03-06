# Generated by Django 4.0.4 on 2022-05-31 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.IntegerField(verbose_name='شماره تلفن')),
                ('number', models.IntegerField(verbose_name='تعداد ')),
                ('date', models.DateField(auto_now=True, verbose_name='تاریخ')),
                ('time', models.TimeField(auto_now=True, verbose_name='ساعت')),
            ],
            options={
                'verbose_name': 'رزرو',
                'verbose_name_plural': 'رزرو ها',
            },
        ),
    ]
