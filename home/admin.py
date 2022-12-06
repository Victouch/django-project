from django.contrib import admin
from .models import Products
from .models import Email
from .models import Search

# Register your models here.
admin.site.register(Products)
admin.site.register(Email)
admin.site.register(Search)
