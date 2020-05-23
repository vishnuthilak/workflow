from django.contrib import admin
from .models import App
from .models import User
from .models import Review,blockwords,Work,WorkAssign,WorkProgress

# Register your models here.


class UserDetailsAdmin(admin.ModelAdmin):    
    list_display = ('name', 'email')
    list_filter = ('name', 'email')
    search_fields = ('name',)


class WorkAdmin(admin.ModelAdmin):    
    list_display = ('workname',)
    list_filter = ('workname',)
    search_fields = ('workname',)


class WorkProgressAdmin(admin.ModelAdmin):    
    list_display = ('detail','status')
    list_filter = ('detail','status')
    search_fields = ('detail',)





admin.site.register(User,UserDetailsAdmin)
admin.site.register(Work,WorkAdmin)
admin.site.register(WorkAssign)
admin.site.register(WorkProgress,WorkProgressAdmin)