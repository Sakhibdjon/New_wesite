from django.contrib import admin
from .models import Position,New

# Register your models here.

# admin.site.register(New)
# admin.site.register(Position)


@admin.register(Position)
class AdminPosition(admin.ModelAdmin):
    list_display= ['id','title']
    list_display_links=['title']
salom men 



@admin.register(New)
class AdminNew(admin.ModelAdmin):
    list_display=['id','name']
    list_display_links= ('name',)
    list_filter=['position']
    search_fields=['name','lang','news']
    # list_per_page = 8
    # list_max_show_all = 15
