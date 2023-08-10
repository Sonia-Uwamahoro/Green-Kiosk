
from django.contrib import admin
from .models import Notice

# Register your models here
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("user_id", "message", "time_stamp")


admin.site.register(Notice, NoticeAdmin)







