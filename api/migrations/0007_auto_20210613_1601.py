# Generated by Django 3.2.4 on 2021-06-13 16:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_chat_utc_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'ordering': ['-chatId']},
        ),
        migrations.AlterField(
            model_name='chat',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('sent', 'Sent')], max_length=20),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatId', models.IntegerField()),
                ('payload', models.TextField(max_length=300, validators=[django.core.validators.RegexValidator('[a-zA-Z]+\\d+\\W+\\_\\-\\\\/\\~\\@\\#\\$\\%\\^\\&\\*\\(\\)\\!\\?')])),
                ('userId', models.IntegerField()),
                ('utc_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('sent', 'Sent')], default='new', max_length=20)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='api.conversation')),
            ],
        ),
    ]