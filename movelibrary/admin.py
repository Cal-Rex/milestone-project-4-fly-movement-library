from django.contrib import admin
from .models import Movement, Tag
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Movement)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('movement_name',)}
    list_display = ('movement_name', 'vid_link')
    search_fields = ['movement_name']


admin.site.register(Tag)

# Alternative method for if multiple arguments or packages
# needed to be added to tables:
# @admin.register(MovementLibrary)
# @admin.register(Tags)
