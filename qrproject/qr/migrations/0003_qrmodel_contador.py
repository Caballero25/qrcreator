# Generated by Django 5.0.2 on 2024-02-21 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0002_qrmodel_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrmodel',
            name='contador',
            field=models.IntegerField(default=0),
        ),
    ]