# Generated by Django 3.1.3 on 2021-05-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]