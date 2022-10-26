# Generated by Django 4.1.2 on 2022-10-25 06:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QRLabs', '0016_alter_qrcodes_created_at_alter_qrcodes_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcodes',
            name='images',
        ),
        migrations.AlterField(
            model_name='qrcodes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 25, 12, 42, 13, 596611)),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('qrcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QRLabs.qrcodes')),
            ],
        ),
    ]
