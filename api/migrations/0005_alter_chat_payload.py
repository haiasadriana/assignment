# Generated by Django 3.2.4 on 2021-06-13 09:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_chat_payload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='payload',
            field=models.TextField(max_length=300, validators=[django.core.validators.RegexValidator('[a-zA-Z]+\\d+\\W+\\_\\-\\\\/\\~\\@\\#\\$\\%\\^\\&\\*\\(\\)\\!\\?')]),
        ),
    ]
