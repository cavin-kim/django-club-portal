from django.shortcuts import render

# Create your views here.
from .models import Member


def member_list(request):
    members = Member.objects.all()
    return render(request, "templates/member_list.html", {"members": members})
