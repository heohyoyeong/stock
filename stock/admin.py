from django.contrib import admin
from .models import User, stockname, stockhistory

admin.site.register(User)
admin.site.register(stockname)

admin.site.register(stockhistory)