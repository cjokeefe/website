# Generated by Django 3.0.5 on 2020-04-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='catchphrase',
            field=models.CharField(default='', max_length=64),
        ),
    ]