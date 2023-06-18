from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Movement, Tag, UserNonAuthField, User
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
            }
        )