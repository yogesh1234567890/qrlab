# Generated by Django 4.1.2 on 2022-10-26 10:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qrcodes',
            fields=[
                ('qrCodeimage', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('uuid', models.CharField(default='man', max_length=1000)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('staticsss', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 10, 26, 10, 15, 54, 269660))),
                ('main_title', models.CharField(default='Untitled', max_length=250)),
                ('qrname', models.CharField(default='Untitled', max_length=250)),
                ('qrData', models.CharField(default='', max_length=10000000000)),
                ('name', models.CharField(max_length=250, null=True)),
                ('type', models.CharField(max_length=250, null=True)),
                ('status', models.CharField(max_length=250, null=True)),
                ('isDynamic', models.BooleanField(default=True)),
                ('firstSet', models.CharField(max_length=250, null=True)),
                ('qrcode', models.CharField(max_length=250, null=True)),
                ('scans', models.IntegerField(default=0)),
                ('archived', models.BooleanField(default=False)),
                ('bg_color', models.CharField(max_length=250, null=True)),
                ('frontcolor', models.CharField(max_length=250, null=True)),
                ('markers_color', models.CharField(max_length=250, null=True)),
                ('marker_out_color', models.CharField(max_length=250, null=True)),
                ('marker_in_color', models.CharField(max_length=250, null=True)),
                ('gradient_color', models.CharField(max_length=250, null=True)),
                ('gradient', models.CharField(max_length=250, null=True)),
                ('framecolor', models.CharField(max_length=250, null=True)),
                ('pattern', models.CharField(max_length=250, null=True)),
                ('marker_out', models.CharField(max_length=250, null=True)),
                ('marker_in', models.CharField(max_length=250, null=True)),
                ('optionlogo', models.CharField(max_length=250, null=True)),
                ('outer_frame', models.CharField(max_length=250, null=True)),
                ('label_font', models.CharField(max_length=250, null=True)),
                ('custom_logo', models.TextField(null=True)),
                ('framelabel', models.CharField(default='scan me', max_length=250)),
                ('no_logo_bg', models.CharField(max_length=250, null=True)),
                ('transparent_code', models.CharField(max_length=250, null=True)),
                ('title', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.TextField(null=True)),
                ('start_date', models.CharField(max_length=250, null=True)),
                ('expiry_date', models.CharField(max_length=250, null=True)),
                ('link_data', models.TextField(null=True)),
                ('email', models.CharField(max_length=250, null=True)),
                ('subject', models.TextField(null=True)),
                ('message', models.TextField(null=True)),
                ('text_data', models.TextField(null=True)),
                ('country_code', models.CharField(max_length=250, null=True)),
                ('phone_number', models.CharField(max_length=250, null=True)),
                ('sms_country_code', models.CharField(max_length=250, null=True)),
                ('sms_phone_number', models.CharField(max_length=250, null=True)),
                ('sms_message', models.TextField(null=True)),
                ('vcard_fname', models.CharField(max_length=250, null=True)),
                ('vcard_lname', models.CharField(max_length=250, null=True)),
                ('vcard_phone_number', models.CharField(max_length=250, null=True)),
                ('vcard_mobile', models.CharField(max_length=250, null=True)),
                ('vcard_email', models.CharField(max_length=250, null=True)),
                ('vcard_web_url', models.CharField(max_length=250, null=True)),
                ('vcard_company', models.CharField(max_length=250, null=True)),
                ('vcard_job_title', models.CharField(max_length=250, null=True)),
                ('vcard_fax', models.CharField(max_length=250, null=True)),
                ('vcard_address', models.TextField(null=True)),
                ('vcard_city', models.CharField(max_length=250, null=True)),
                ('vcard_post_code', models.CharField(max_length=250, null=True)),
                ('vcard_country', models.CharField(max_length=250, null=True)),
                ('whatsapp_country_code', models.CharField(max_length=250, null=True)),
                ('whatsapp_phone_number', models.CharField(max_length=250, null=True)),
                ('whatsapp_message', models.TextField(null=True)),
                ('network_name', models.CharField(max_length=250, null=True)),
                ('network_type', models.CharField(max_length=250, null=True)),
                ('network_password', models.TextField(null=True)),
                ('wifi_hidden', models.TextField(null=True)),
                ('social_facebook_link_title', models.CharField(max_length=250, null=True)),
                ('social_twitter_link_title', models.CharField(max_length=250, null=True)),
                ('social_instagram_link_title', models.CharField(max_length=250, null=True)),
                ('social_linkedin_link_title', models.CharField(max_length=250, null=True)),
                ('social_pinterest_link_title', models.CharField(max_length=250, null=True)),
                ('social_youtube_link_title', models.CharField(max_length=250, null=True)),
                ('social_snapchat_link_title', models.CharField(max_length=250, null=True)),
                ('social_reddit_link_title', models.CharField(max_length=250, null=True)),
                ('social_facebook_link', models.CharField(max_length=250, null=True)),
                ('social_twitter_link', models.CharField(max_length=250, null=True)),
                ('social_instagram_link', models.CharField(max_length=250, null=True)),
                ('social_linkedin_link', models.CharField(max_length=250, null=True)),
                ('social_pinterest_link', models.CharField(max_length=250, null=True)),
                ('social_youtube_link', models.CharField(max_length=250, null=True)),
                ('social_snapchat_link', models.CharField(max_length=250, null=True)),
                ('social_reddit_link', models.CharField(max_length=250, null=True)),
                ('social_bg_color', models.CharField(max_length=250, null=True)),
                ('social_logo', models.TextField(null=True)),
                ('video', models.TextField(null=True)),
                ('pdf', models.FileField(null=True, upload_to='pdf/')),
                ('folder_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QRLabs.folder')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
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
