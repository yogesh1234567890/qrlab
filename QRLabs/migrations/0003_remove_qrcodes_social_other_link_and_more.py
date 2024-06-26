# Generated by Django 4.1.2 on 2022-10-29 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QRLabs', '0002_remove_qrcodes_social_logo_qrcodes_full_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcodes',
            name='social_other_link',
        ),
        migrations.RemoveField(
            model_name='qrcodes',
            name='social_other_link_title',
        ),
        migrations.CreateModel(
            name='OtherSocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_link_title', models.CharField(max_length=250, null=True)),
                ('social_link', models.CharField(max_length=250, null=True)),
                ('social_icon', models.ImageField(null=True, upload_to='social_icons')),
                ('qrcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QRLabs.qrcodes')),
            ],
        ),
    ]
