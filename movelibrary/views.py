from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Movement, Tag, UserOneRepMax, User, UserNonAuthField, PromoVideo
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
        last_movement = get_object_or_404(
            UserNonAuthField, user_id=request.user.id
        ).last_movement
        print("last movement", last_movement)
        promo_list = PromoVideo.objects.filter()
        promo_list_length = len(promo_list) - 1
        print(promo_list)
        print(promo_list_length)
        promo_pick = random.randint(0, promo_list_length)
        print(promo_pick)
        promo_video = promo_list[promo_pick]
        print(promo_video)
        bookmarks = Movement.objects.filter(bookmarks__id=request.user.id)
        one_rm_records = UserOneRepMax.objects.filter(
            user_id=request.user.id
        ).order_by(
            "-date_recorded"
        )
        return render(
            request,
            'index.html',
            {
                "user_name": user_name,
                "user_new": user_new,
                "promo_video": promo_video,
                "last_movement": last_movement,
                "one_rm_records": one_rm_records,
                "bookmarks": bookmarks,
                "movement_library_list": movement_library_list,
            }
        )


class MovementDetail(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request, slug, *args, **kwargs):
        movement_from_library = get_object_or_404(Movement, slug=slug)
        user = get_object_or_404(User, id=request.user.id)
        bookmarks = Movement.objects.filter(bookmarks__id=request.user.id)
        user_last_movement = UserNonAuthField()
        user_lm_check = UserNonAuthField.objects.filter(
            user_id__id=request.user.id
        )
        print(len(user_lm_check))
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
                "library_movement": movement_from_library,
                "one_rm_records": one_rm_records,
                "bookmarks": bookmarks,
                "bookmarked": bookmarked,
                "one_rm_form": OneRmForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        movement_from_library = get_object_or_404(Movement, slug=slug)
        one_rm_records = movement_from_library.one_rm_list.filter(
            user_id=request.user.id
        ).order_by("-date_recorded")
        bookmarked = False
        if movement_from_library.bookmarks.filter(
            id=self.request.user.id
        ).exists():
            bookmarked = True

        one_rm_form = OneRmForm(data=request.POST)

        if one_rm_form.is_valid():
            one_rm = one_rm_form.save(commit=False)
            one_rm.user_id = request.user
            one_rm.movement = movement_from_library
            one_rm.save()
            messages.add_message(request, SUCCESS, f"new {one_rm.one_rep_max} KG 1-Rep Max recorded!")
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
    login_url = '/accounts/login/'

    def get(self, request):
        bookmarks = Movement.objects.filter(bookmarks__id=request.user.id)
        query = request.GET.get('query').title()
        queries = query.split()
        results = Movement.objects.filter(movement_name__contains=query)
        return render(
            request,
            'search_results.html',
            {
                'results': results,
                "bookmarks": bookmarks,
            }
        )


class MovementBookmark(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def post(self, request, slug):
        movement = get_object_or_404(Movement, slug=slug)
        if movement.bookmarks.filter(id=request.user.id).exists():
            movement.bookmarks.remove(request.user)
        else:
            movement.bookmarks.add(request.user)
        return HttpResponseRedirect(reverse('movement_detail', args=[slug]))


class BookmarksList(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'

    model = Movement

    def get(self, request, *args, **kwargs):
        bookmarks = Movement.objects.filter(bookmarks__id=request.user.id)
        return render(
            request,
            'bookmarks_list.html',
            {
                "bookmarks": bookmarks
            }
        )

    template_name = 'bookmarks_list.html'
    context_object_name = 'bookmarked_movement'
    paginate_by = 8


class OneRepMaxRecords(LoginRequiredMixin, generic.ListView):
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
    record = get_object_or_404(UserOneRepMax, id=record_id)
    movement_from_library = get_object_or_404(Movement, slug=slug)
    if request.method == 'POST':
        one_rm_form = OneRmForm(data=request.POST, instance=record)
        if one_rm_form.is_valid():
            one_rm = one_rm_form.save(commit=False)
            one_rm.user_id = request.user
            one_rm.movement = movement_from_library
            one_rm.save()
            messages.add_message(request, SUCCESS, f'1-RM from {one_rm.date_recorded.strftime("%m/%j/%y at %H:%M")} amended.')
            return redirect('movement_detail', slug=slug)
    form = OneRmForm(instance=record)
    context = {
        'form': form
    }
    return redirect('movement_detail', slug=slug)


def delete_one_rm(request, slug, record_id):
    record = get_object_or_404(UserOneRepMax, id=record_id)
    record.delete()
    return redirect('movement_detail', slug=slug)


class EditProfile(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
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
        bookmarks = Movement.objects.filter(bookmarks__id=request.user.id)
        user = get_object_or_404(User, id=request.user.id)
        user_first_name = user.first_name
        user_last_name = user.last_name

        name_edit_form = NameEditForm(data=request.POST, instance=user)

        if name_edit_form.is_valid():
            new_name = name_edit_form.save(commit=False)
            new_name.user_id = request.user
            new_name.save()
            messages.add_message(request, SUCCESS, 'Profile Successfully updated')
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
