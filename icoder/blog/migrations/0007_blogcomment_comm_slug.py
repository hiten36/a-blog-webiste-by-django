# Generated by Django 3.1.6 on 2021-02-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210206_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='comm_slug',
            field=models.CharField(default='', max_length=90),
        ),
    ]
