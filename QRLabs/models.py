from datetime import datetime
from email.policy import default
from os import link
from django.contrib.auth.models import User
from django.db import models


class Folder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Qrcodes(models.Model):
    qrCodeimage = models.ImageField(upload_to='images/', blank=True, null=True)
    uuid = models.CharField(max_length=1000,default='man')
    id = models.AutoField(primary_key=True)
    staticsss=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    main_title = models.CharField(max_length=250, default='Untitled')
    qrname = models.CharField(max_length=250, default='Untitled')
    qrData=models.TextField(default='')
    name = models.CharField(max_length=250, null=True)
    type = models.CharField(max_length=250, null=True)
    status = models.CharField(max_length=250, null=True)
    isDynamic = models.BooleanField(default=True)
    firstSet = models.CharField(max_length=250, null=True)
    qrcode = models.CharField(max_length=250, null=True)
    scans = models.IntegerField(default=0)
    archived = models.BooleanField(default=False)
    # Qrcode Styling Fields
    bg_color = models.CharField(max_length=250, null=True)
    frontcolor = models.CharField(max_length=250, null=True)
    markers_color = models.CharField(max_length=250, null=True)
    marker_out_color = models.CharField(max_length=250, null=True)
    marker_in_color = models.CharField(max_length=250, null=True)
    gradient_color = models.CharField(max_length=250, null=True)
    gradient = models.CharField(max_length=250, null=True)
    framecolor = models.CharField(max_length=250, null=True)
    pattern = models.CharField(max_length=250, null=True)
    marker_out = models.CharField(max_length=250, null=True)
    marker_in = models.CharField(max_length=250, null=True)
    optionlogo = models.CharField(max_length=250, null=True)
    outer_frame = models.CharField(max_length=250, null=True)
    label_font = models.CharField(max_length=250, null=True)
    custom_logo = models.TextField(null=True)
    framelabel = models.CharField(max_length=250, default='scan me')
    no_logo_bg = models.CharField(max_length=250, null=True)
    transparent_code = models.CharField(max_length=250, null=True)
    # Model Relations
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    folder_id = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True)
    # Type Expiry Management
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.TextField(null=True)
    start_date = models.CharField(max_length=250, null=True)
    expiry_date = models.CharField(max_length=250, null=True)
    # Type link
    link_data = models.TextField(null=True)
    # Type email
    email = models.CharField(max_length=250, null=True)
    subject = models.TextField(null=True)
    message = models.TextField(null=True)
    # Type text
    text_data = models.TextField(null=True)
    # Type call
    country_code = models.CharField(max_length=250, null=True)
    phone_number = models.CharField(max_length=250, null=True)
    # Type sms
    sms_country_code = models.CharField(max_length=250, null=True)
    sms_phone_number = models.CharField(max_length=250, null=True)
    sms_message = models.TextField(null=True)
    # Type Vcard
    vcard_fname = models.CharField(max_length=250, null=True)
    vcard_lname = models.CharField(max_length=250, null=True)
    vcard_phone_number = models.CharField(max_length=250, null=True)
    vcard_mobile = models.CharField(max_length=250, null=True)
    vcard_email = models.CharField(max_length=250, null=True)
    vcard_web_url = models.CharField(max_length=250, null=True)
    vcard_company = models.CharField(max_length=250, null=True)
    vcard_job_title = models.CharField(max_length=250, null=True)
    vcard_fax = models.CharField(max_length=250, null=True)
    vcard_address = models.TextField(null=True)
    vcard_city = models.CharField(max_length=250, null=True)
    vcard_post_code = models.CharField(max_length=250, null=True)
    vcard_country = models.CharField(max_length=250, null=True)
    # Type Whatsapp
    whatsapp_country_code = models.CharField(max_length=250, null=True)
    whatsapp_phone_number = models.CharField(max_length=250, null=True)
    whatsapp_message = models.TextField(null=True)
    # Type Wifi
    network_name = models.CharField(max_length=250, null=True)
    network_type = models.CharField(max_length=250, null=True)
    network_password = models.TextField(null=True)
    wifi_hidden = models.TextField(null=True)
    # Type Social Link
    full_name = models.CharField(max_length=250, null=True)
    title = models.TextField(null=True)
    email = models.EmailField(max_length=250, null=True)
    phone_number = models.CharField(max_length=250, null=True)
    website = models.CharField(max_length=250, null=True)
    social_facebook_link_title = models.CharField(max_length=250, null=True)
    social_twitter_link_title = models.CharField(max_length=250, null=True)
    social_instagram_link_title = models.CharField(max_length=250, null=True)
    social_linkedin_link_title = models.CharField(max_length=250, null=True)
    social_pinterest_link_title = models.CharField(max_length=250, null=True)
    social_youtube_link_title = models.CharField(max_length=250, null=True)
    social_snapchat_link_title = models.CharField(max_length=250, null=True)
    social_reddit_link_title = models.CharField(max_length=250, null=True)
    
    social_facebook_link = models.CharField(max_length=250, null=True)
    social_twitter_link = models.CharField(max_length=250, null=True)
    social_instagram_link = models.CharField(max_length=250, null=True)
    social_linkedin_link = models.CharField(max_length=250, null=True)
    social_pinterest_link = models.CharField(max_length=250, null=True)
    social_youtube_link = models.CharField(max_length=250, null=True)
    social_snapchat_link = models.CharField(max_length=250, null=True)
    social_reddit_link = models.CharField(max_length=250, null=True)

    social_bg_color = models.CharField(max_length=250, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True)
    # Type Video
    video = models.TextField(null=True)
    # Type pdf
    pdf = models.FileField(upload_to='pdf/', null=True)

    # def __str__(self):
    #     return self.type

class OtherSocialLinks(models.Model):
    social_link_title = models.CharField(max_length=250, null=True)
    social_link = models.CharField(max_length=250, null=True)
    social_icon = models.ImageField(upload_to='social_icons', null=True)
    qrcode = models.ForeignKey(Qrcodes, on_delete=models.CASCADE)

    def __str__(self):
        return self.social_link_title

class Images(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    qrcode = models.ForeignKey(Qrcodes, on_delete=models.CASCADE)