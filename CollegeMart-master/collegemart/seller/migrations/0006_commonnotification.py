# Generated by Django 2.0.9 on 2018-12-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_request_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='commonNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='', max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
