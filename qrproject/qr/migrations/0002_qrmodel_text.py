# Generated by Django 5.0.2 on 2024-02-21 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrmodel',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
