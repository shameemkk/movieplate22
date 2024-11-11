from django.contrib import admin

# Register your models here.
# movie/admin.py
from django.contrib import admin
from .models import movieDetails
from django.contrib.auth.models import User

# Register the movieDetails model
@admin.register(movieDetails)
class MovieDetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'releaseDate','type','director')
    search_fields = ('title',)

# Optionally, you can customize the User admin if needed
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name','is_staff')
    search_fields = ('username', 'email')

# Unregister the default User admin and register the custom User admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)