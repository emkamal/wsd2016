from django.contrib import admin
from .models import Blog, Post

# Note: If you want to use the admin interface you need a superuser.
# I can be made with "manage.py createsuperuser"

# This is the simple way of adding a model to the admin
# interface
admin.site.register(Post)

# ...And this is a more complicated one. We have only added a convenience
# thing - prepopulation of the slug field from the title when using the admin
# interface.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog, BlogAdmin)
