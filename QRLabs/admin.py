from django.contrib import admin
from .models import Qrcodes, Images
from .models import Folder

# Register your models here.

admin.site.register(Qrcodes)
admin.site.register(Folder)
admin.site.register(Images)