# Generated by Django 2.2.7 on 2019-11-15 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20191114_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logininfo',
            old_name='link',
            new_name='login_link',
        ),
        migrations.AddField(
            model_name='logininfo',
            name='reset_link',
            field=models.CharField(blank=True, max_length=225, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='logininfo',
            name='fails',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
