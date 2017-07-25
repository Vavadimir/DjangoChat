from django.contrib import admin
from .models import Comments
# Register your models here.

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'pub_date', 'comment')

admin.site.register(Comments, CommentsAdmin)