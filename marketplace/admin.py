from django.contrib import admin
from .models import Furniture, FurnitureImage

# Inline admin for uploading multiple images
class FurnitureImageInline(admin.TabularInline):
    model = FurnitureImage
    extra = 4  # number of empty forms for additional images
    fields = ['image']  # Only show the image upload field

# Furniture admin setup
class FurnitureAdmin(admin.ModelAdmin):
    inlines = [FurnitureImageInline]
    list_display = ('title', 'price', 'age')

# Register the admin
admin.site.register(Furniture, FurnitureAdmin)

# Customize admin site header and titles
admin.site.site_header = "Antik Hoelzli Admin"
admin.site.site_title = "Antik Hoelzli Admin Portal"
admin.site.index_title = "Welcome to the Antik Hoelzli Dashboard"