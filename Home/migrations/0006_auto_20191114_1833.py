# Generated by Django 2.2.7 on 2019-11-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20191114_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logininfo',
            name='link',
            field=models.CharField(blank=True, max_length=225, null=True, unique=True),
        ),
    ]
