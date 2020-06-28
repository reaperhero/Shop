from django.contrib import admin
from common.models import Users, Types, Goods,Orders,Details
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'gender', 'address', 'phone', 'email','addtime']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 10


admin.site.register(Users, UserAdmin)
admin.site.register(Types)
admin.site.register(Goods)
admin.site.register(Orders)
admin.site.register(Details)