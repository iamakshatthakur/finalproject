from django.contrib import admin
from video.models import VideoComment,categorylist,Item
from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass


# Register your models here
admin.site.register(categorylist)
admin.site.register(Item,MyModelAdmin)
admin.site.register(VideoComment)
