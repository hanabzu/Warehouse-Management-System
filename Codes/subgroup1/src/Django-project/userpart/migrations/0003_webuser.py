# Generated by Django 3.1.3 on 2021-05-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpart', '0002_auto_20210529_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('user_pw', models.CharField(max_length=10)),
            ],
        ),
    ]
