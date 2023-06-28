from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Movement, Tag, UserNonAuthField, UserOneRepMax, User
from .forms import OneRmForm
from django.contrib.auth.decorators import login_required

# Create your views here.


class Landing(generic.ListView):  # change to DetailView when figured out
    model = Movement
    template_name = 'index.html'
    context_object_name = 'movement'


# class Landing(generic.DetailView):

#     login = request.session.get(User)

#     def __getitem__(login):
#         if not Login.is_authenticated:
#             return redirect('login')
#         else:
#             user = request.User.id
#             user_last_movement = UserNonAuthField.last_movement
#             model = Movement
#             template_name = 'index.html'
#             context_object_name = 'last_movement_viewed'


# class login(View):
#     template_name = "account/login.html"


class MovementDetail(View):
    # needing to go out now, but so i can troubleshoot later:
    # can't get one rep max for movement to show up on the page.
    # haven't checked if the record of 20 for barbell push press has been successfully logged to the database  # noqa
    # checked the variable "one_rm_records" via print statement to see it's value (it's empty)  # noqa
    # need to go and check the admin panel to see f any data recorded. and then work from there. may need to go back to editing the form  # noqa
    def get(self, request, slug, *args, **kwargs):
        movement_from_library = get_object_or_404(Movement, slug=slug)
        one_rm_records = movement_from_library.one_rm_list.filter(
            user_id=request.user.id
        ).order_by("-date_recorded")
        print("HEYYYYYYYYYYYYYY", one_rm_records)
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
                "bookmarked": bookmarked,
                "one_rm_form": OneRmForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):

        movement_from_library = get_object_or_404(Movement, slug=slug)
        one_rm_records = movement_from_library.one_rm_list.filter(
            id=request.user.id
        ).order_by("-date_recorded")
        bookmarked = False
        if movement_from_library.bookmarks.filter(
            id=self.request.user.id
        ).exists():
            bookmarked = True

        one_rm_form = OneRmForm(data=request.POST)
        if one_rm_form.is_valid():
            one_rm_form.instance.user_id = request.user.id
            one_rep_max = one_rm_form.save(commit=False)
            one_rep_max.movement = movement_from_library
            one_rep_max.save()
        else:
            one_rm_form = OneRmForm()

        return render(
            request,
            "movement.html",
            {
                "library_movement": movement_from_library,
                "one_rm_records": one_rm_records,
                "bookmarked": bookmarked,
                "one_rm_form": One_Rm_Form,
            }
        )


class MovementSearch(generic.ListView):

    def get(self, request):
        query = request.GET.get('query').title()
        queries = query.split()
        results = Movement.objects.filter(movement_name__contains=query)
        print(results)
        return render(request, 'search_results.html', {'results': results})


class MovementBookmark(View):

    # the name of the function is actually calling the POST method.
    def post(self, request, slug):
        movement = get_object_or_404(Movement, slug=slug)
        if movement.bookmarks.filter(id=request.user.id).exists():
            movement.bookmarks.remove(request.user)
        else:
            movement.bookmarks.add(request.user)
        return HttpResponseRedirect(reverse('movement_detail', args=[slug]))


class BookmarksList(generic.ListView):

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


class OneRepMaxRecords(generic.ListView):

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

    def post(self, request, UserOneRepMax_id):
        one_rm_record = get_object_or_404(UserOneRepMax,)


class AddOneRmRecord(View):
    def post(self, request, slug):
        movement = get_object_or_404(Movement, slug=slug)
        form = OneRmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movement_detail")
