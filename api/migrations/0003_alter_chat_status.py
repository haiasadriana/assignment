# Generated by Django 3.2.4 on 2021-06-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_chat_utc_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('sent', 'Sent')], default='new', max_length=20),
        ),
    ]
