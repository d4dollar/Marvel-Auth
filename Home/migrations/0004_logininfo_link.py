# Generated by Django 2.2.7 on 2019-11-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191114_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='logininfo',
            name='link',
            field=models.CharField(default='NO_LINK', max_length=225),
        ),
    ]
