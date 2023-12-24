from django.contrib import admin
from .models import dnld


@admin.register(dnld)
class dnld_admin(admin.ModelAdmin):
    list_display = ('title', 'author')
