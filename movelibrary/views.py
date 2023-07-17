from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Movement, Tag, UserOneRepMax, User
from .models import UserNonAuthField, PromoVideo, SocialMediaCard
from .forms import OneRmForm, NameEditForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import random


"""
Message Variables:
"""
DEBUG = 10
INFO = 20
SUCCESS = 25
WARNING = 30
ERROR = 40


class Landing(LoginRequiredMixin, generic.ListView):
    """
    View for ths index template.
    contains view-code for the following features
    (in order of code blocks):
    - Check to see if a user is a new user, generates appropriate
      welcome message depending on outcome
    - full list of movements (to be used by search feature)
    - Show the last movement a user has/had viewed
    - Show a promotional video as hero content
    - Show list of the user's bookmarked movements
    - Show the last 1-Rep-Max a user recorded
    - Social media panel view, which has been repurposed
      to being a class-booking view
    """
    login_url = '/accounts/login/'

    model = Movement
    template_name = 'index.html'
    context_object_name = 'movement'

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=request.user.id)
        user_name = user.first_name
        date_joined = user.date_joined.strftime("%m/%j/%y %H:%M")
        last_login = user.last_login.strftime("%m/%j/%y %H:%M")
        user_new = False
        if last_login == date_joined:
            user_new = True

        movement_library_list = Movement.objects.filter()
        alphabetized = sorted(
            movement_library_list,
            key=lambda item: item.movement_name
        )
        movement_library_list = alphabetized

        movement_viewed = False
        last_movement_check = UserNonAuthField.objects.filter(
            user_id=request.user.id
        )
        if len(last_movement_check) < 1:
            library_count = len(movement_library_list) - 1
            move_pick = random.randint(0, library_count)
            last_movement = movement_library_list[move_pick]
        else:
            movement_viewed = True
            user_lm_record = get_object_or_404(
                UserNonAuthField,
                user_id=request.user.id
            ).last_movement
            last_movement = get_object_or_404(Movement, slug=user_lm_record)

        promo_list = PromoVideo.objects.filter()
        promo_list_length = len(promo_list) - 1
        promo_pick = random.randint(0, promo_list_length)
        promo_video = promo_list[promo_pick]

        bookmarks = Movement.objects.filter(bookmarks__id=request.user.id)

        orm_recorded = False
        one_rm_records = UserOneRepMax.objects.filter(
            user_id=request.user.id
        ).order_by(
            "-date_recorded"
        )
        if len(one_rm_records) < 1:
            library_count = len(movement_library_list) - 1
            move_pick = random.randint(0, library_count)
            last_orm = movement_library_list[move_pick]
        else:
            orm_recorded = True
            last_record = one_rm_records[0].movement
            last_orm = get_object_or_404(Movement, id=last_record.id)

        sm_cards = SocialMediaCard.objects.filter()
        choice = random.randint(0, len(sm_cards) - 1)
        insta_card = sm_cards[choice]

        return render(
            request,
            'index.html',
            {
                "user_name": user_name,
                "user_new": user_new,
                "promo_video": promo_video,
                "last_movement": last_movement,
                "movment_viewed": movement_viewed,
                "one_rm_records": one_rm_records,
                "last_orm": last_orm,
                "bookmarks": bookmarks,
                "movement_library_list": movement_library_list,
                "insta_card": insta_card,
            }
        )


class Library(LoginRequiredMixin, generic.ListView):
    """
    Views for the library page
    contains:
        - Bookmarks list for footer menu
        - full list of movements,
          alphabetised to be shown as a list on the page
    """
    login_url = '/accounts/login/'

    model = Movement
    template_name = 'index.html'
    context_object_name = 'movement'

    def get(self, request, *args, **kwargs):
        movement_library_list = Movement.objects.filter()
        alphabetized = sorted(
            movement_library_list,
            key=lambda item: item.movement_name
        )
        movement_library_list = alphabetized

        bookmarks = Movement.objects.filter(bookmarks__id=request.user.id)
        return render(
            request,
            'library.html',
            {
                "movement_library_list": movement_library_list,
                "bookmarks": bookmarks,
            }
        )


class MovementDetail(LoginRequiredMixin, View):
    """
    View for the movement.html template for when
    someone is viewing a specific movement.
    contains both GET and POST handlers.
    """
    login_url = '/accounts/login/'

    def get(self, request, slug, *args, **kwargs):
        """
        GET contains the following:
        - full list of movements (for search)
        - the specific movement the user requested to view
        - bookmarked movements of the user (for footer menu)
        - checks the last movement of a user, if none exists
        a record is created, else, the recorded is updated
        record the selected movement
        - the 1-rm records of the requested movement
        - conditional check to see if movement is bookmarked
        """
        movement_library_list = Movement.objects.filter()
        alphabetized = sorted(
            movement_library_list,
            key=lambda item: item.movement_name
        )
        movement_library_list = alphabetized

        movement_from_library = get_object_or_404(Movement, slug=slug)
        user = get_object_or_404(User, id=request.user.id)

        bookmarks = Movement.objects.filter(bookmarks__id=request.user.id)

        user_last_movement = UserNonAuthField()
        user_lm_check = UserNonAuthField.objects.filter(
            user_id__id=request.user.id
        )
        if len(user_lm_check) == 0:
            user_last_movement.user_id = user
            user_last_movement.last_movement = movement_from_library.slug
            user_last_movement.save()
        else:
            user_lm_check = get_object_or_404(
                UserNonAuthField,
                user_id__id=request.user.id
            )
            user_lm_check.last_movement = movement_from_library.slug
            user_lm_check.save()

        one_rm_records = movement_from_library.one_rm_list.filter(
            user_id=request.user.id
        ).order_by("-date_recorded")

        bookmarked = False
        if movement_from_library.bookmarks.filter(
            id=self.request.user.id
        ).exists():
            bookmarked = True

        return render(
            request,
            "movement.html",
            {
                "movement_library_list": movement_library_list,
                "library_movement": movement_from_library,
                "one_rm_records": one_rm_records,
                "bookmarks": bookmarks,
                "bookmarked": bookmarked,
                "one_rm_form": OneRmForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        """
        POST contains the following:
        - bookmark check/uncheck function
        - handling of the add 1-rm form
        - adding of a new 1-rep max record
        """
        movement_from_library = get_object_or_404(Movement, slug=slug)

        bookmarked = False
        if movement_from_library.bookmarks.filter(
            id=self.request.user.id
        ).exists():
            bookmarked = True

        one_rm_records = movement_from_library.one_rm_list.filter(
            user_id=request.user.id
        ).order_by("-date_recorded")

        one_rm_form = OneRmForm(data=request.POST)

        if one_rm_form.is_valid():
            one_rm = one_rm_form.save(commit=False)
            one_rm.user_id = request.user
            one_rm.movement = movement_from_library
            one_rm.save()
            messages.add_message(
                request,
                SUCCESS,
                f"new {one_rm.one_rep_max} KG 1-Rep Max recorded!"
            )
            return redirect('movement_detail', slug=slug)

        return render(
            request,
            "movement.html",
            {
                "library_movement": movement_from_library,
                "one_rm_records": one_rm_records,
                "bookmarked": bookmarked,
                "one_rm_form": one_rm_form,
            }
        )


class MovementSearch(LoginRequiredMixin, generic.ListView):
    """
    view for the search results template
    conatins:
    - full lst of movements
    - User bookmarks
    - handler for entered query in search field
    - results gnerated based on the filtered list
      of movements
    """
    login_url = '/accounts/login/'

    def get(self, request):
        movement_library_list = Movement.objects.filter()
        alphabetized = sorted(
            movement_library_list,
            key=lambda item: item.movement_name
        )
        movement_library_list = alphabetized

        bookmarks = Movement.objects.filter(bookmarks__id=request.user.id)
        query = request.GET.get('query').title()
        queries = query.split()
        results = Movement.objects.filter(movement_name__contains=query)
        return render(
            request,
            'search_results.html',
            {
                'movement_library_list': movement_library_list,
                'results': results,
                "bookmarks": bookmarks,

            }
        )


class MovementBookmark(LoginRequiredMixin, View):
    """
    handles the function of bookmarking a movement
    """
    login_url = '/accounts/login/'

    def post(self, request, slug):
        movement = get_object_or_404(Movement, slug=slug)
        if movement.bookmarks.filter(id=request.user.id).exists():
            movement.bookmarks.remove(request.user)
        else:
            movement.bookmarks.add(request.user)
        return HttpResponseRedirect(reverse('movement_detail', args=[slug]))


class OneRepMaxRecords(LoginRequiredMixin, generic.ListView):
    """
    handles the viewing of the users list of one-rep maxes
    for a specific movement when viewing that movement
    """
    login_url = '/accounts/login/'

    def get(self, request, slug, *args, **kwargs):
        movement = get_object_or_404(Movement, slug=slug)
        one_rm_records = UserOneRepMax.objects.filter(
            user_id=request.user.id
            ).filter(~Q(movement=Movement.slug))
        return render(
            request,
            "movement_detail",
            {
                "one_rm_records": one_rm_records
            }
        )


def edit_one_rm(request, slug, record_id):
    """
    function that handles the editing form for
    1-rep maxes.
    """
    record = get_object_or_404(UserOneRepMax, id=record_id)
    movement_from_library = get_object_or_404(Movement, slug=slug)
    if request.method == 'POST':
        one_rm_form = OneRmForm(data=request.POST, instance=record)
        if one_rm_form.is_valid():
            one_rm = one_rm_form.save(commit=False)
            one_rm.user_id = request.user
            one_rm.movement = movement_from_library
            one_rm.save()
            one_rm_date = one_rm.date_recorded.strftime("%m/%j/%y at %H:%M")
            messages.add_message(
                request,
                SUCCESS,
                f'1-RM from {one_rm_date} amended.'
            )
            return redirect('movement_detail', slug=slug)

    form = OneRmForm(instance=record)
    context = {
        'form': form
    }
    return redirect('movement_detail', slug=slug)


def delete_one_rm(request, slug, record_id):
    """
    function that handles the deletion of 1-rep maxes
    """
    record = get_object_or_404(UserOneRepMax, id=record_id)
    record.delete()
    return redirect('movement_detail', slug=slug)


class EditProfile(LoginRequiredMixin, View):
    """
    class that handles the viewing and updating of
    a user's profile information.
    currently, for safety and assessment, this class
    only fcuses on the editing of a user's name.
    """
    login_url = '/accounts/login/'

    def get(self, request):
        """
        get request which handles retrival of profile data
        in addition to standard base functions on the view
        """
        bookmarks = Movement.objects.filter(bookmarks__id=request.user.id)
        user = get_object_or_404(User, id=request.user.id)
        user_first_name = user.first_name
        user_last_name = user.last_name

        name_edit_form = NameEditForm(instance=user)
        return render(
            request,
            'profile.html',
            {
                "name_edit_form": name_edit_form,
                "bookmarks": bookmarks,
                "user_first_name": user_first_name,
                "user_last_name": user_last_name,
            }
        )

    def post(self, request):
        """
        handles the post data of the edit form
        """
        bookmarks = Movement.objects.filter(bookmarks__id=request.user.id)
        user = get_object_or_404(User, id=request.user.id)
        user_first_name = user.first_name
        user_last_name = user.last_name

        name_edit_form = NameEditForm(data=request.POST, instance=user)

        if name_edit_form.is_valid():
            new_name = name_edit_form.save(commit=False)
            new_name.user_id = request.user
            new_name.save()
            messages.add_message(
                request,
                SUCCESS,
                'Profile Successfully updated'
            )
            return redirect('edit_profile',)

        return render(
            request,
            'profile.html',
            {
                "name_edit_form": name_edit_form,
                "bookmarks": bookmarks,
                "user_first_name": user_first_name,
                "user_last_name": user_last_name,
            }
        )
