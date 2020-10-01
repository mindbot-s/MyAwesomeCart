# Generated by Django 3.1 on 2020-08-19 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200819_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderupdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(default='', max_length=500)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
