from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Movement, Tag, UserNonAuthField

# Create your views here.


class LastMovement(generic.ListView):
    model = Movement
    template_name = 'index.html'
    paginate_by = 1
