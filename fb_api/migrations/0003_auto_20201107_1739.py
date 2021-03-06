# Generated by Django 3.1.3 on 2020-11-07 17:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fb_api', '0002_message_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
