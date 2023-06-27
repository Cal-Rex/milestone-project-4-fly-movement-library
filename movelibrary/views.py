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

    def get(self, request, slug, *args, **kwargs):
        movement_from_library = get_object_or_404(Movement, slug=slug)
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
                "bookmarked": bookmarked,
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
