from django.contrib import admin

# Register your models here.
from .models import Hostlist
from portconfig.models import Portlist
admin.site.register(Hostlist)
admin.site.register(Portlist)