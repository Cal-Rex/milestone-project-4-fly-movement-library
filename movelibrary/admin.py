from django.contrib import admin
from .models import Movement, Tag, UserMovementNotes, UserOneRepMax, UserNonAuthField, PromoVideo  # noqa
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Movement)
class MovementAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('movement_name',)}
    list_display = ('movement_name', 'vid_link')
    search_fields = ['movement_name']


@admin.register(PromoVideo)
class PromoVideoAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('promo_name',)}
    list_display = ('promo_name', 'vid_link')
    search_fields = ['promo_name']


@admin.register(Tag)
class TagAdmin(SummernoteModelAdmin):

    list_display = ('movement',)


@admin.register(UserNonAuthField)
class UserNonAuthFieldAdmin(SummernoteModelAdmin):

    list_display = ('user_id', 'last_movement', 'terms',)


@admin.register(UserMovementNotes)
class UserMovementNotesAdmin(SummernoteModelAdmin):

    list_display = ('user_id', 'movement',)


@admin.register(UserOneRepMax)
class UserOneRepMaxAdmin(SummernoteModelAdmin):

    list_display = ('user_id', 'movement', 'one_rep_max', 'date_recorded',)


# Alternative method for if multiple arguments or packages
# needed to be added to tables:
# @admin.register(MovementLibrary)
# @admin.register(Tags)
