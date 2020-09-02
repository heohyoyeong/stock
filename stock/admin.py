from django.contrib import admin
from .models import User, stockname, stockhistory, Chat

admin.site.register(User)
admin.site.register(stockname)

admin.site.register(stockhistory)

admin.site.register(Chat)