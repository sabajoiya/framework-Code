from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.models import *

from django.contrib.sites.models import Site

class profileAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email']


admin.site.register(Profile, profileAdmin)
admin.site.unregister(Group)
admin.site.register(Post)


