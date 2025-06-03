from django.contrib import admin
from .models import Furniture

admin.site.register(Furniture)
admin.site.site_header = "Antik Hoelzli Admin"
admin.site.site_title = "Antik Hoelzli Admin Portal"
admin.site.index_title = "Welcome to the Antik Hoelzli Dashboard"