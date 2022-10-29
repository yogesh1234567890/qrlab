from django.contrib import admin
from .models import Qrcodes, Images, OtherSocialLinks
from .models import Folder

# Register your models here.

admin.site.register(Qrcodes)
admin.site.register(Folder)
admin.site.register(Images)
admin.site.register(OtherSocialLinks)