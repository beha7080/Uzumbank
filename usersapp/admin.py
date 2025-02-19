# from django.contrib import admin
# from . models import User
#
# admin.site.register(User)
# # Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User

# admin.site.register(User)  # ❌ BU QATORNI O‘CHIRING YOKI IZOHGA OLING


from django.contrib import admin
from .models import AdminStatus

@admin.register(AdminStatus)
class AdminStatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'updated_at')

